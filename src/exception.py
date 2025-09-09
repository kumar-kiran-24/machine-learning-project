import sys 

def error_mesage_deatil(error,erroe_detail:sys):
    _,_,exc_tb=erroe_detail.exe_info()
    file_name=exc_tb.tb_frame.f_code.co_filname
    error_meaage="Error cocured in python script name[{0}] line number [{1}] erroe messaeg[{2}].format() "
    file_name,exc_tb.tb_lineo,str(error)
     
class CustomExeception(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_meaagse=error_mesage_deatil(error_message,error_detail=error_detail)