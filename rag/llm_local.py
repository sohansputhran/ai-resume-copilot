from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

MODEL_PATH = "TheBloke/Mistral-7B-Instruct-v0.1-GPTQ"

def load_llm():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        device_map="auto",
        trust_remote_code=True,
        revision="main"
    )
    return pipeline("text-generation", 
                    model=model, 
                    tokenizer=tokenizer, 
                    max_new_tokens=512, 
                    do_sample=True,
                    temperature=0.7,
                    top_p=0.95
                    )

llm_pipeline = load_llm()

def generate_response(prompt):
    return llm_pipeline(prompt)[0]['generated_text']