from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/send_post', methods=['GET'])
def send_post():
    # Define the FastAPI endpoint URL
    url = 'http://localhost:8000/get_desc/12345'

    # Prepare evidence files
    evidence_files = [
        ('evidence_files', ('annotated_1321_vanta_s_1.xlsx', open('annotated_1321_vanta_s_1.xlsx', 'rb'))),
        ('evidence_files', ('annotated_2707_test_file_3 (6).pdf', open('annotated_2707_test_file_3 (6).pdf', 'rb')))
    ]

    # Prepare policy files
    policy_files = [
        ('policy_files', ('vect.png', open('vect.png', 'rb')))]

    # Prepare form data (control fields)
    form_data = {
        'name': 'Access Control',
        'description': 'Describes the policies related to access management.',
        'category': 'Security'
    }

    # Combine evidence files, policy files
    all_files = evidence_files + policy_files

    try:
        # Send POST request to FastAPI endpoint
        response = requests.post(url, files=all_files, data=form_data)
        response_data = response.json()

        # Return the FastAPI response as JSON
        return jsonify({
            "status": "success",
            "response": response_data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(port=5000)
