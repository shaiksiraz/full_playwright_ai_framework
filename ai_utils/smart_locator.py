# ai_utils/smart_locator.py
from sentence_transformers import SentenceTransformer, util
from transformers import BertTokenizer, BertModel
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')

def suggest_locator(old_text, all_candidates):
    # Convert old_text to tensor
    old_text_inputs = tokenizer.encode_plus(
        old_text,
        add_special_tokens=True,
        max_length=512,
        return_attention_mask=True,
        return_tensors='pt',
        truncation=True
    )

    # Convert all_candidates to tensors
    candidate_tensors = []
    for candidate in all_candidates:
        candidate_inputs = tokenizer.encode_plus(
            candidate,
            add_special_tokens=True,
            max_length=512,
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        candidate_embeddings = bert_model(candidate_inputs['input_ids'], attention_mask=candidate_inputs['attention_mask']).last_hidden_state[:, 0, :]
        candidate_tensors.append(candidate_embeddings)

    # Calculate similarity between old_text and all_candidates
    old_text_embedding = model.encode([old_text])
    similarity = util.pytorch_cos_sim(old_text_embedding, torch.cat(candidate_tensors))

    # Get the index of the most similar candidate
    best_match_index = similarity.argmax()
    return all_candidates[best_match_index]