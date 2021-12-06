import fasttext
import nltk
import os
import sys
from nltk.corpus import stopwords
import warnings
#Preprocesar (Cambiar para que sea sobre string y no dataframe)
def remove_stopwords(data: str) -> str:
    """Remove stop words from list of tokenized words"""
    new_words = []
    words = data.split(' ')
    for word in words:
        if word not in stopwords.words('spanish'):
            new_words.append(word)
        elif word == 'no':
            new_words.append(word)
    return ' '.join(new_words)

def preprocessing(data: str)-> str:
    #Reemplazar URLs por url
    data = data.replace('http\S+|www.\S+', 'url')
    #Eliminar referencia a imagenes
    data = data.replace('\[cid\S+', '')
    #Reemplazar emails por mail
    data = data.replace('\S+@\S+', 'mail')
    #Pasar a minúsculas
    data = data.lower()
    #Eliminar puntuación
    data = data.replace('[^\w\s]', '')
    #Eliminar números
    data = data.replace('\d+', '') 
    return data

def get_and_preprocess_input() -> str:
    #Pedir asunto al usuario
    assignment = input("Por favor, escriba el asunto de su consulta: ")
    #Pedir descripción al usuario
    description = input("\nAhora, escriba una descripcion breve de su caso: ")
    data = assignment + ' ' + description
    data = remove_stopwords(data)
    data = preprocessing(data)
    return data

""" 
    pre: el modelo preentrenado debe encontrarse en el directorio especificado
"""
def predict_category(data: str) -> tuple:
    model = fasttext.load_model("model_dsit_val.ftz")
    return model.predict(data)
    
def run():
    data = get_and_preprocess_input()
    predicted_category, prediction_probability = predict_category(data)
    prediction_probability = prediction_probability[0]
    predicted_category = predicted_category[0].replace('_(tiempos_sujetos_a_variación_por_protocolos_de_bioseguridad)','')
    predicted_category = predicted_category.replace('__label__','')
    predicted_category = predicted_category.replace('_',' ')
    print('\nSu caso sera asignado a la categoria de: ' + predicted_category)
    print('\nLa probabilidad de que su caso pertenezca a la categoria ' + predicted_category +  
          ' es de: ' + str(round(prediction_probability, ndigits=2)*100))
    print('\nSi la probabilidad es baja, un agente del DSIT se encargara de reasignar su caso para solucionar su problema')
    print("\nGracias a esta asignación su petición sera solucionada rapidamente, estaremos en contacto!")
    
#Correr modelo
if __name__ == '__main__':
    #os.chdir(os.path.dirname(sys.path[0]))
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    os.chdir(__location__)
    print(os.getcwd())
    print('Asignando categoria al caso para su posterior analisis')
    fasttext.FastText.eprint = lambda x: None
    run()
    
