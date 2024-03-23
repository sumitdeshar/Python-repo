from survey import AnonymousSurvey

# def test_store_single_response():
#     question = 'What language did you first learn to speak?'
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response('Newari')
#     assert 'Newari','Nepali' in language_survey.responses
    
def test_store_multiple_response():
    question = 'What language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)
    responses = ['Newari','Nepali','English','Hindi','little Japansese','little Russian']
    for response in responses:
        language_survey.store_response(response)
        
    for response in responses:
        assert response in language_survey.responses

#  a fixture helps set up a test environment
import pytest 
from survey import AnonymousSurvey 
@pytest.fixture 
def language_survey(): 
    """A survey that will be available to all test 
    functions.""" 
    question = "What language did you first learn to speak?" 
    language_survey = AnonymousSurvey(question) 
    return language_survey 
#Note: key point is to used a decorator and then using the object initializing function name as parameter in test funtion 
# then decorator check the funtion and passes the resource/object around
def test_store_single_response(language_survey): 
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses 
def test_store_three_responses(language_survey): 
    """Test that three individual responses are stored 
    properly.""" 
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
         language_survey.store_response(response) 
    for response in responses:
        assert response in language_survey.responses