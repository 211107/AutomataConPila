import re

class StackConditional:
    def __init__(self):
        self.stack = []
        self.stopWord = ""
        self.tripAnalysis = []
        self.tripAnalysisError = []
        
    def clearData(self):
        self.stack = []
        self.stopWord = ""
        self.tripAnalysis = []
        self.tripAnalysisError = []
                
        
    def transition(self, estado, text):        
        if estado == "q_rechazo":                        
            return "q_rechazo"

        if estado == "q0":            
            if (text == "si"):                                
                self.tripAnalysis.append("SiS10")
                self.tripAnalysis.append("Si S10")                
                return "q1"
            else:                
                self.stopWord = text
                return "q_rechazo"
        else:
            self.stopWord = text        
            
        if estado == "q1":            
            if (re.match("^[a-zA-Z0-9]+$", text)):                
                self.tripAnalysis.append("S10")
                self.tripAnalysis.append("S9 Lc")
                self.tripAnalysis.append("S9")
                self.tripAnalysis.append("S8 R")
                self.tripAnalysis.append("S8")
                self.tripAnalysis.append("S7 La")
                self.tripAnalysis.append("S7")
                self.tripAnalysis.append("S6 E")
                self.tripAnalysis.append("S6")
                self.tripAnalysis.append("S5 Lc")
                self.tripAnalysis.append("S5")
                self.tripAnalysis.append("S4 R")
                self.tripAnalysis.append("S4")
                self.tripAnalysis.append("S3 LA")
                self.tripAnalysis.append("S3")
                self.tripAnalysis.append("S2 N")
                self.tripAnalysis.append("S2")
                self.tripAnalysis.append("S1 Ig")
                self.tripAnalysis.append("S1")
                self.tripAnalysis.append("R Mq")
                self.tripAnalysis.append("R")
                self.tripAnalysis.append("MR|mR|NR|∈ ")
                self.tripAnalysis.append("Mq")                
                return "q2"
            else:
                self.stopWord = text                
                return "q_rechazo"
        else:
            self.stopWord = text     

        if (estado == "q2" and text in [">", "==", "<", ">=", "<="] ):   
                self.tripAnalysis.append("> ig")
                self.tripAnalysis.append("Ig")
                self.tripAnalysis.append('= N')                                                                   
                return "q3"                                       
        else:
            self.stopWord = text                

        if estado == "q3":                 
            value = re.match('([0-9])*', text)            
            if (value):                              
                self.tripAnalysis.append("N")
                self.tripAnalysis.append("0..9 LA")                                                                      
                return "q4"
            else:                
                self.stopWord = text                          
                return "q_rechazo"
        else:
            self.stopWord = text

        if estado == "q4" and text == "{":            
            self.tripAnalysis.append("R")
            self.tripAnalysis.append("LR|NR|∈ LC")
            self.tripAnalysis.append("LC")
            self.tripAnalysis.append("LR|NR|∈ E")
            self.tripAnalysis.append("E")
            self.tripAnalysis.append("sino LA")
            self.tripAnalysis.append("{ R")
            self.tripAnalysis.append("R")
            self.tripAnalysis.append("0..9 LC")
            self.tripAnalysis.append("LC")
            self.tripAnalysis.append("}")                                        
            return "q_accept"                    
        else:
            self.stopWord = text               
                   
             
        return "q_rechazo"        
        
    def validateInput(self, lineCode:str):        
        actualState = "q0"                    
        lineCode = re.sub(' +', ' ', lineCode).strip()     
        lineCode = lineCode.split(" ");        
        for word in lineCode:            
            actualState = self.transition(actualState, word)

        return actualState == "q_accept"

    def getStack(self):
        return self.stack
    
    def getTripAnalysis(self):
        return self.tripAnalysis
    
    def getTripAnalysisError(self):        
        return self.tripAnalysisError
     
    def getStopWord(self):
        return f"Error en: {self.stopWord}"

