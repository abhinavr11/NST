from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = 'microsoft/DialoGPT-large'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_res(user_message):
    user_input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')

    # generated a response by the model
    bot_output_ids = model.generate(user_input_ids, pad_token_id=tokenizer.eos_token_id)

    # decode previous message to text
    start_of_bot_message = user_input_ids.shape[-1]
    bot_message = tokenizer.decode(bot_output_ids[:, start_of_bot_message:][0], skip_special_tokens=True)

    return bot_message
