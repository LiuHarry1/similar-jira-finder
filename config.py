import os

class db_config:
    USER_NAME = ""
    PASSWORD = ""
    HOST = ""
    INSTANCE_NAME = ""

class BaseConfig():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMP_DIR = os.path.join(ROOT_DIR, "temp")
    NLP_DIR = os.path.join(ROOT_DIR, "nlp")
    NLP_NER_DIR = os.path.join(NLP_DIR, "NER")
    TRADITIONAL_ML_DIR = os.path.join(ROOT_DIR, "traditional_ml")
    AI_SERVICE_DATA_PATH = os.path.join(ROOT_DIR, "..","ai-service-data")

    # ===================nlp_tc_config Start =====================
    DATASET = os.path.join(ROOT_DIR, 'nlp', 'text_classification', 'dataset')
    IMDB_DATASET = os.path.join(DATASET, 'imdb')
    IMDB_RAW_DATA = os.path.join(ROOT_DIR, "..", "ai-service-data/data/aclImdb")
    TEXT_CNN = os.path.join(ROOT_DIR, 'nlp', 'text_classification', 'text_cnn')
    TEXT_CNN_MODEL = os.path.join(TEXT_CNN, 'model')
    WORD_2_VECTOR = os.path.join(ROOT_DIR, 'nlp', 'word2vector')
    GLOVE_PATH = os.path.join(WORD_2_VECTOR, 'glove')

    # ===================nlp_tc_config End=====================

    # ===================nlp_ner_config Start =====================
    NER_PATH = os.path.join( ROOT_DIR , 'nlp', 'NER')
    conll2003_RAW_DATA = os.path.join(ROOT_DIR, "..", "ai-service-data/data/conll2003")
    conll2003_DATASET_PATH = os.path.join(NER_PATH, 'dataset')
    conll2003_word2idx = os.path.join(conll2003_DATASET_PATH, 'word2idx.json')
    conll2003_idx2Label = os.path.join(conll2003_DATASET_PATH, 'idx2Label.json')
    conll2003_DATASET =  os.path.join(conll2003_DATASET_PATH, 'dataset')
    CNN_MODEL_PATH=os.path.join(NER_PATH, 'model', 'cnn', 'model')
    conll2003_MAX_LEN =  128

    # ===================nlp_ner_config End =====================

    # ===================tflite_config Start =====================

    TFLITE = os.path.join(ROOT_DIR, 'tflite')
    TFLITE_NLP = os.path.join(TFLITE, 'nlp')
    TFLITE_MODEL= os.path.join(TFLITE_NLP, 'model')
    SENTIMENT_ANALYSIS= os.path.join(TFLITE_MODEL, 'sentiment_analysis')
    NER = os.path.join(TFLITE_MODEL, 'ner')
    TFLITE_DATASET = os.path.join(TFLITE_NLP, 'dataset')
    TFLITE_IMDB = os.path.join(TFLITE_DATASET, 'imdb')

    # ===================tflite_config End =====================

    NNLM_MODEL = os.path.join(AI_SERVICE_DATA_PATH, "model", "nnlm-en-dim50_2")

    # ===================email category Start =====================



    NLTK_DATA = os.path.join(AI_SERVICE_DATA_PATH, "model", "nltk")


    # ===================email category End =====================



class DevelopmentConfig(BaseConfig):
    TRAINED_MODEL_PATH = "/app/1001090000/data/models"
    EMAIL_CLASSIFICATION = os.path.join(TRAINED_MODEL_PATH, "email_classification")
    MINILM_MODEL = os.path.join(TRAINED_MODEL_PATH, "all-MiniLM-L6-v2")
    UNIVERSAL_SENTENCE_ENCODER_MODEL = os.path.join(TRAINED_MODEL_PATH, "universal-sentence-encoder_4")
    NLM_EN_DIM50_2 = os.path.join(TRAINED_MODEL_PATH, "nnlm-en-dim50_2")
    ENG_FRA_MODEL = os.path.join(TRAINED_MODEL_PATH, "eng_fra_model")
    EMAIL_CATEGORY_DATA = os.path.join(TRAINED_MODEL_PATH, "data", "email-category")
    PROMPT_ENGINEERING_URL = "http://localhost:5000"

class LocalConfig(BaseConfig):
    MODEL_PATH = os.path.join(BaseConfig.AI_SERVICE_DATA_PATH, "model")
    TRAINED_MODEL_PATH = os.path.join(BaseConfig.AI_SERVICE_DATA_PATH, "trained_models")
    EMAIL_CLASSIFICATION = os.path.join(TRAINED_MODEL_PATH, "email_classification")
    MINILM_MODEL = os.path.join(MODEL_PATH, "all-MiniLM-L6-v2")
    NLM_EN_DIM50_2 = os.path.join(MODEL_PATH, "nnlm-en-dim50_2")
    UNIVERSAL_SENTENCE_ENCODER_MODEL = os.path.join(MODEL_PATH, "universal-sentence-encoder_4")

    ENG_FRA_MODEL = os.path.join(TRAINED_MODEL_PATH, "eng_fra_model")
    EMAIL_CATEGORY_DATA =  os.path.join(BaseConfig.AI_SERVICE_DATA_PATH, "data", "email-category")
    PROMPT_ENGINEERING_URL = "http://localhost:5000"



def get_env(var, default=None):
    try:
        return os.environ[var]
    except:
        return default

ai_env = get_env("AI_ENV")

if ai_env == "local":
    Config = LocalConfig()
elif ai_env == "dev":
    Config = DevelopmentConfig()
else:
    Config = LocalConfig()
print("AI_ENV:", ai_env)
print("Config:", Config)

