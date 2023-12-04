import re

class StackPrint:
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
        print("sss")
        if estado == "q_rechazo":                        
            return "q_rechazo"

        if estado == "q0":            
            if (text == "imprimir"):                
                self.stack.append(text)
                self.tripAnalysis.append("ST4")
                self.tripAnalysis.append("S")
                self.tripAnalysis.append("imprimir T4")
                return "q1"
            else:                
                self.stopWord = text             
                return "q_rechazo"
        else:
            self.stopWord = text        
            
        if estado == "q1":
            if (text == "("):    
                self.tripAnalysis.append("T4")
                self.tripAnalysis.append("T1 T2")
                self.tripAnalysis.append("T1")
                self.tripAnalysis.append("PA LL")
                self.tripAnalysis.append("PA")                 
                self.stack.append(text)        
                return "q2"
            else:                
                self.stopWord = text                   
                return "q_rechazo"
        else:
            self.stopWord = text                    

        if estado == "q2":            
            if (re.match('^"([a-zA-Z]| |[0-9]|.|,)*"+$', text)):                                                         
                self.stack.append(text)
                self.tripAnalysis.append("( LL")
                self.tripAnalysis.append("LL")
                self.tripAnalysis.append('"" T2')
                self.tripAnalysis.append("T2")
                self.tripAnalysis.append("R T3")
                self.tripAnalysis.append("R")
                self.tripAnalysis.append("MR|mR|NR T3")
                self.tripAnalysis.append("T3")
                self.tripAnalysis.append("LL PC")
                self.tripAnalysis.append("LL")
                self.tripAnalysis.append('"" PC')                
                return "q3"
            else:                
                self.stopWord = text                           
                return "q_rechazo"
        else:
            self.stopWord = text

        if estado == "q3":            
            if (text == ")"):                
                self.stack.append(text)              
                return "q_accept"
            else:                
                self.stopWord = text             
                return "q_rechazo"
        else:
            self.stopWord = text               
                   
             
        return "q_rechazo"        
        
    def validateInput(self, input:str):
        actualState = "q0"            
        patron = re.compile(r'([a-zA-Z0-9]+|\(|\)|"[^"]*")')        
        text = [match for match in patron.findall(input) if match]    
        print("sss")
        print(text)           
        for word in text:            
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

