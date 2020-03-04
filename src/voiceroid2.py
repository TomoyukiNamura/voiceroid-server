# -*- coding: utf-8 -*-

import pywinauto

class VoiceRoid2(object):
    
    def __init__(self):
                
        # エレメント名の登録
        self.voiceroid2_name_list   = ["VOICEROID2", "VOICEROID2*"]
        self.texteditview_name_list = ["TextEditView"]
        self.textbox_name_list      = ["TextBox"]
        self.button_name_list       = ["Button"]
        self.textblock_name_list    = ["TextBlock"]
        self.playbutton_name_list   = ["再生"] 
        
        # コントロール初期化
        self.textbox_control    = None
        self.playbutton_control = None
        
        # voiceroid2のelement取得
        self._get_voiceroid2_ele()
        
        
    def _search_child_byclassname(self, class_name_list, uiaElementInfo, target_all = False):
        target = []
        # 全ての子要素検索
        for child_ele in uiaElementInfo.children():
            # ClassNameの一致確認
            if child_ele.class_name in class_name_list:
                if target_all == False:
                    return child_ele
                else:
                    target.append(child_ele)
        if target_all == False:
            # 無かったらNone
            return None
        else:
            return target


    def _search_child_byname(self, name_list, uiaElementInfo):
        # 全ての子要素検索
        for child_ele in uiaElementInfo.children():
            # Nameの一致確認
            if child_ele.name in name_list:
                return child_ele
        # 無かったらNone
        return None
    
    
    def _search_flist_byname(self, parent_name_list, child_name_list, ele_list):
        for parent_ele in ele_list:
            # elementを捜索
            child_ele = self._search_child_byclassname(parent_name_list, parent_ele)
            if child_ele.name in child_name_list:
                return parent_ele
        # 無かったらNone
        return None
    
    
    def _get_voiceroid2_ele(self):
        
        # デスクトップのエレメント
        parent_uia_element = pywinauto.uia_element_info.UIAElementInfo()   

        # voiceroidを捜索する
        self.voiceroid2_ele = self._search_child_byname(self.voiceroid2_name_list, parent_uia_element)
        
        if self.voiceroid2_ele is not None:
            self.is_run = True
            print("Log: Success to find VOICEROID2!!")
            self.utterance("おぉ世界よ、ごきげんよう！")
            
        else:
            self.is_run = False
            print("Error: Failed to find VOICEROID2.")
        
    
    def _get_controls(self):
        
        # テキスト要素のElementInfoを取得
        texteditview_ele = self._search_child_byclassname(self.texteditview_name_list, self.voiceroid2_ele)
        textbox_ele = self._search_child_byclassname(self.textbox_name_list,texteditview_ele)        

        # ボタン取得
        button_ele_list = self._search_child_byclassname(self.button_name_list,texteditview_ele,target_all = True)
        playbutton_ele = self._search_flist_byname(self.textblock_name_list, self.playbutton_name_list, button_ele_list)
        
        # テキスト・ボタンコントロール取得
        self.textbox_control = pywinauto.controls.uia_controls.EditWrapper(textbox_ele)
        self.playbutton_control = pywinauto.controls.uia_controls.ButtonWrapper(playbutton_ele)
    
    
    def _hold_controls(self):
        hold_textbox_control = self.textbox_control is not None
        hold_playbutton_control = self.playbutton_control is not None
        return (hold_textbox_control and hold_playbutton_control)

    
    def utterance(self,text):
        
        # コントロールの取得
        if self._hold_controls() == False:
            self._get_controls()
        
        # テキスト登録
        self.textbox_control.set_edit_text(text)
        
        # 再生ボタン押下
        self.playbutton_control.click()
        
