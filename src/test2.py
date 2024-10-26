# test_interactive_quiz.py
from confidence_quiz import ConfidenceQuiz
import time  # Add pauses to make sure we can see everything

def clear_screen():
    print("\n" * 50)  # Print many newlines to "clear" screen

def main():
    clear_screen()
    print("\n🌟 WORKPLACE CONFIDENCE QUIZ 🌟")
    print("--------------------------------")
    print("\nThis quiz will assess your workplace confidence.")
    print("You'll see 5 questions, one at a time.")
    input("\n>>> Press Enter to begin <<<")
    
    quiz = ConfidenceQuiz()
    answers = []
    
    for q in quiz.questions:
        clear_screen()
        print(f"\n📝 QUESTION {q['id']} OF 5")
        print("-" * 40)
        time.sleep(1)  # Pause to ensure question is visible
        
        # Display question
        print(f"\n{q['question']}")
        time.sleep(1)
        
        # Display options
        print("\nYour options:")
        for letter, text in q['options'].items():
            print(f"\n{letter}) {text}")
            time.sleep(0.5)  # Slight pause between options
        
        # Get answer
        while True:
            answer = input("\n>>> Your answer (A, B, or C): ").upper()
            if answer in ['A', 'B', 'C']:
                answers.append(answer)
                break
            else:
                print("❌ Please enter only A, B, or C!")
        
        print("\n✅ Answer recorded! Loading next question...")
        time.sleep(1)
    
    # Calculate and display results
    clear_screen()
    print("\n🎯 CALCULATING YOUR RESULTS...")
    time.sleep(1)
    
    results = quiz.calculate_score(answers)
    
    print("\n🌟 YOUR QUIZ RESULTS 🌟")
    print("-" * 40)
    
    print(f"\n📊 Score: {results['score']} out of {results['max_score']}")
    print(f"📈 Percentage: {results['percentage']:.1f}%")
    print(f"🎯 Confidence Level: {results['feedback']['level']}")
    
    input("\n>>> Press Enter to see your feedback <<<")
    
    print("\n💪 YOUR STRENGTHS:")
    for strength in results['feedback']['strengths']:
        print(f"✓ {strength}")
        time.sleep(0.5)
    
    input("\n>>> Press Enter to see recommendations <<<")
    
    print("\n📋 RECOMMENDED NEXT STEPS:")
    for step in results['feedback']['next_steps']:
        print(f"→ {step}")
        time.sleep(0.5)
    
    input("\n>>> Press Enter to see scoring guide <<<")
    
    print("\n📊 SCORING GUIDE:")
    print("-" * 40)
    print("11-15 points (70-100%): High Confidence")
    print("8-10 points (50-69%): Growing Confidence")
    print("5-7 points (0-49%): Emerging Confidence")
    
    input("\n>>> Press Enter to finish quiz <<<")
    print("\nThank you for taking the Workplace Confidence Quiz!")

if __name__ == "__main__":
    main()