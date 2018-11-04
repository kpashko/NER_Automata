import os
import collections

ner_tags = collections.Counter()

corpus_root = "/Users/kostyapashko/Desktop/gmb-2.2.0" # Make sure you set the proper path to the unzipped corpus

for root, dirs, files in os.walk(corpus_root):
    for filename in files:
        if filename.endswith(".tags"):
            with open(os.path.join(root, filename), 'rb') as file_handle:
                file_content = file_handle.read().decode('utf-8').strip()
                annotated_sentences = file_content.split('\n\n')  # Split sentences
                for annotated_sentence in annotated_sentences:
                    annotated_tokens = [seq for seq in annotated_sentence.split('\n') if seq]  # Split words

                    standard_form_tokens = []

                    for idx, annotated_token in enumerate(annotated_tokens):
                        annotations = annotated_token.split('\t')  # Split annotation
                        word, tag, ner = annotations[0], annotations[1], annotations[3]

                        # Get only the primary category
                        if ner != 'O':
                            ner = ner.split('-')[0]
                        if ner == "per":
                            print(word)
                        ner_tags[ner] += 1

#print(ner_tags)
# Counter({u'O': 1146068, u'geo': 58388, u'org': 48094, u'per': 44254, u'tim': 34789, u'gpe': 20680, u'art': 867, u'eve': 709, u'nat': 300})

print(ner_tags["per"])
print("Words=", sum(ner_tags.values()))
