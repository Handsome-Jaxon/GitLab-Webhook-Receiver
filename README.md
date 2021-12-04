# GitLab-Webhook-Receiver
GitLab event with Line notify 

The infrastructure is constructed on AWS API gateway & Lambda.
You need to setup POST API gateway and integrate with Lambda so that you can receive the webhook.  
<br/><br/>

You will need to paste your API gateway URL in the GitLab Webhook URL field  
![image](https://user-images.githubusercontent.com/78006007/144711287-42435dae-1965-49a2-8808-eab4bf8190e8.png)


And input your line notify access token in ****"lambda_function.py"**** below to finish the integration  
![image](https://user-images.githubusercontent.com/78006007/144711339-cd5caae9-7c46-432d-a43e-bcfacb1a3758.png)
