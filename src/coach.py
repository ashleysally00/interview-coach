from datetime import datetime
import json
from pathlib import Path

class InterviewCoach:
    def __init__(self):
        # Load feedback templates
        self.feedback_templates = {
            "leadership": [
                "Your example demonstrates {strength}. Consider providing more details about {area}.",
                "Strong demonstration of {strength}. To improve, try focusing more on {area}.",
            ],
            "negotiation": [
                "Good job highlighting {strength}. You could enhance your response by addressing {area}.",
                "Excellent point about {strength}. Consider also discussing {area}.",
            ]
        }
        
        # Common strengths and areas for improvement
        self.strengths = {
            "leadership": [
                "clear decision-making process",
                "team collaboration",
                "problem-solving abilities",
                "initiative taken"
            ],
            "negotiation": [
                "preparation and research",
                "value communication",
                "confidence in presentation",
                "strategic thinking"
            ]
        }
        
        self.improvement_areas = {
            "leadership": [
                "quantifiable results",
                "delegation strategies",
                "stakeholder communication",
                "long-term planning"
            ],
            "negotiation": [
                "market research data",
                "specific achievements",
                "alternative proposals",
                "follow-up planning"
            ]
        }

    def analyze_response(self, question: str, response: str, category: str) -> dict:
        """Analyze interview response and provide feedback."""
        # Basic response analysis
        word_count = len(response.split())
        
        # Select relevant strengths and areas for improvement
        selected_strengths = []
        selected_areas = []
        
        # Simple analysis based on keywords
        for strength in self.strengths[category]:
            if any(keyword in response.lower() for keyword in strength.split()):
                selected_strengths.append(strength)
                
        for area in self.improvement_areas[category]:
            if not any(keyword in response.lower() for keyword in area.split()):
                selected_areas.append(area)
        
        # Ensure we have at least some feedback
        if not selected_strengths:
            selected_strengths = [self.strengths[category][0]]
        if not selected_areas:
            selected_areas = [self.improvement_areas[category][0]]
        
        # Calculate confidence score
        confidence_score = min(100, max(0, (
            (word_count / 50) * 20 +  # Length factor
            len(selected_strengths) * 20 -  # Strengths bonus
            len(selected_areas) * 10  # Areas for improvement penalty
        )))
        
        # Generate feedback
        feedback = {
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'response': response,
            'strengths': selected_strengths[:3],  # Top 3 strengths
            'areas_for_improvement': selected_areas[:2],  # Top 2 areas
            'confidence_score': confidence_score,
            'action_items': [
                f"Include more specific examples about {area}" 
                for area in selected_areas[:2]
            ],
            'tips': [
                "Use the STAR method: Situation, Task, Action, Result",
                "Quantify your achievements where possible",
                "Focus on your direct contributions and leadership"
            ]
        }
        
        return feedback

    def save_feedback(self, feedback: dict):
        """Save feedback to a JSON file for history tracking."""
        history_path = Path(__file__).parent.parent / 'data' / 'feedback_history.json'
        
        # Load existing history
        if history_path.exists():
            with open(history_path, 'r') as f:
                history = json.load(f)
        else:
            history = []
        
        # Add new feedback
        history.append(feedback)
        
        # Save updated history
        with open(history_path, 'w') as f:
            json.dump(history, f, indent=2)