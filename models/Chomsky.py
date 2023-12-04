# Importación de las pilas
from stack.StackPatronVar import StackPatronVar
from stack.StackPatronFuncion import StackPatronFunction
from stack.StackWhile import StackWhile
from stack.StackRead import StackRead
from stack.StackPrint import StackPrint
from stack.StackConditional import StackConditional
from stack.StackElse import StackElse

# Instancia de las pilas 
myStackPatronVar = StackPatronVar()
myStackPatronFunction = StackPatronFunction()
myStackWhile = StackWhile()
myStackRead = StackRead()
myStackPrint = StackPrint()
myStackConditional = StackConditional()
myStackElse = StackElse()

# Importación de librarías
import re

class Chomsky:          
    
    
    def matchValidator(self, reference,rule):
        patron = re.compile(r'['+rule+']', re.IGNORECASE)
        coincidencias = patron.findall(reference)        
        length = len(set(coincidencias))  
        return length >= 1   
        
    def classifyInput(self,lineCode: str):        
        
        data = [];
        
   
                    
        word = lineCode.split(" ")[0]
        
        if(word == "romper"):                                
                data =[
                    "valido",
                    [
                        "Data ya descrita en la declaración del mientras"
                    ],
                    word
                ]
                return data
        
        if(word == "var"): 
            myStackPatronVar.clearData()
            response = myStackPatronVar.validateInput(lineCode)            
            if(response==True):
                tripAnalysis = myStackPatronVar.getTripAnalysis()                
                data=["Valido",tripAnalysis,lineCode]
                return data
            else:
                stopWord = myStackPatronVar.getStopWord()
                tripAnalysisError = myStackPatronVar.getTripAnalysisError()                
                data=["No Valido",tripAnalysisError,stopWord,lineCode]
                return data
        
        if(word == "fun"):
            myStackPatronFunction.clearData()
            response = myStackPatronFunction.validateInput(lineCode)            
            if(response==True):
                tripAnalysis = myStackPatronFunction.getTripAnalysis()                
                data=["Valido",tripAnalysis,lineCode]
                return data
            else:
                stopWord = myStackPatronFunction.getStopWord()
                tripAnalysisError = myStackPatronFunction.getTripAnalysisError()                
                data=["No Valido",tripAnalysisError,stopWord,lineCode]
                return data
            
        if(word == "mientras"):
            myStackWhile.clearData()
            response = myStackWhile.validateInput(lineCode)            
            if(response==True):
                tripAnalysis = myStackWhile.getTripAnalysis()                
                data=["Valido",tripAnalysis,lineCode]
                return data
            else:
                stopWord = myStackWhile.getStopWord()
                tripAnalysisError = myStackWhile.getTripAnalysisError()                
                data=["No Valido",tripAnalysisError,stopWord,lineCode]
                return data            

        coincidence =  self.matchValidator(word,'e') 
        
        if(coincidence > 0):                         
            myStackRead.clearData()
            response = myStackRead.validateInput(lineCode)            
            if(response==True):
                tripAnalysis = myStackRead.getTripAnalysis()                            
                data=["Valido",tripAnalysis,lineCode]
                return data
            else:
                stopWord = myStackRead.getStopWord()
                tripAnalysisError = myStackRead.getTripAnalysisError()                
                data=["No Valido",tripAnalysisError,stopWord,lineCode]
                return data   
                             
        coincidence =  self.matchValidator(word,'nprmr')                    
        print("Validando para imprimir")   
        if(coincidence > 0):      
            print(True)                                     
            myStackPrint.clearData()
            response = myStackPrint.validateInput(lineCode)            
            if(response==True):
                tripAnalysis = myStackPrint.getTripAnalysis()                          
                data=["Valido",tripAnalysis,lineCode]
                return data
            else:
                stopWord = myStackPrint.getStopWord()
                tripAnalysisError = myStackPrint.getTripAnalysisError()                
                data=["No Valido",tripAnalysisError,stopWord,lineCode]
                return data
        else:
            print(False)            
                       
        if(word == "si"):        
            myStackConditional.clearData()
            response = myStackConditional.validateInput(lineCode)            
            if(response==True):
                tripAnalysis = myStackConditional.getTripAnalysis()                
                data=["Valido",tripAnalysis,lineCode]
                return data
            else:
                stopWord = myStackConditional.getStopWord()
                tripAnalysisError = myStackConditional.getTripAnalysisError()                
                data=["No Valido",tripAnalysisError,stopWord,lineCode]
                return data
        print(lineCode)
        if(lineCode == "}" or word =="}"):
            data = [
                "Valido",
                ["Data ya descrita"],
                lineCode
            ]         
            return data                        
            

                
        if(len(lineCode)==0):
            return None
        coincidence =  self.matchValidator(word,'var')        
        if (coincidence):            
            stopWord = f"Error en: {word}"
            data=["No valido",stopWord,lineCode]
            return data
        else:
            data = ["No valido","Erro inesperado",lineCode.split(" ")]
            return data
        

        


                
        
                
        
        