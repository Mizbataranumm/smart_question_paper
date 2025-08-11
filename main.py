import pandas as pd

def load_questions():
    print("🔄 Loading CSV...")
    df = pd.read_csv('data/sample_questions.csv')
    print(f"✅ Loaded {len(df)} questions")
    return df

def generate_question_paper():
    print("📄 Generating question paper...")
    questions = load_questions()

    # Select 5 random questions
    selected = questions.sample(5)

    print("\n📘 Your Generated Question Paper:\n")
    for i, row in selected.iterrows():
        print(f"{i+1}. {row['question']} [Marks: {row['marks']}]")

if __name__ == '__main__':
    print("🚀 Starting Smart Question Paper Generator...")
    generate_question_paper()
