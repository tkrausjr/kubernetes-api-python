# https://www.google.com/search?q=build+a+simple+kubernetes+web+based+application+k8s+api&sca_esv=492d03d456b59a14&rlz=1C5GCCA_en&udm=50&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpV6Bbbmx4QVaoKkiRQ2jlwvCHF0Eqz8cUq4JjDCZnrJG3IQ9hSM-GoYfSAqo_zJgC8GHuEE9ehM7VlFnv8pyn_4gwgnnAqmsxpqy1E8YGqcDS9cptS67pcIpPqn4IMgzGMeCqJHb-zTRxeehyYmiPr22wi7vtH9t-0PG7m_AIs8H2mc6dH6OEJ2wczdXosTAaf6qSFA&aep=1&ntc=1&sa=X&ved=2ahUKEwjgusfchI6SAxVPMlkFHUvhMbUQ2J8OegQIBRAE&biw=1704&bih=963&dpr=2&aic=0&mstk=AUtExfASzBrNy4FZFO8ASFIrrjvkTaSOwyJrfh-l5t5IxCElfFQOEepkTRzNR1zKAfK0cuaSokPfj8T7xuwdoQ-D0PYubJZJUBwl5-jaDdo8kwnba8nn2Y3rclW10RbwqvuHRK-13SUZJWMpoGjCnK1HlArAMAi3zF2D6hq6vy9pg5w3DPoPYNJ5t4iVaYTONWM2yLXaTW_oLKxURj6BnQmS3_NN9THVIkf2SuOUKfYlMEKbgPdo0tHMsEB31Q&csuir=1&atvm=2
from flask import Flask
from kubernetes import client, config

app = Flask(__name__)

@app.route('/')
def get_pods():
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    return {"pods": [pod.metadata.name for pod in pods.items]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
