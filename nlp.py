from transformers import pipeline
def classify(text):
# Load the pipeline for sequence classification
 classifier = pipeline('text-classification', model='Sarvina/Uzbek_Logistics_message_classifier', tokenizer='Sarvina/Uzbek_Logistics_message_classifier')

# Example sentence to test
 sentence = text

# Get the prediction for the sentence
 result = classifier(sentence)
 if result[0]['label']=='LABEL_1':
  return text
 else:
  return 'nothing'
print(classify('qayerga'))