from flask import Flask, render_template

app = Flask(__name__)
app.config["TESTING"] = False

portfolio = {
    "name": "Satyam Yadav",
    "title": "Cloud Platform Engineer",
    "city": "Pune",
    "email": "satyam.a.yadav@capgemini.com",
    "mobile": "6397392081",
    "intro": "Cloud Platform Engineer with 4+ years of experience in AWS, Azure, Kubernetes, Terraform, CloudFormation, and DevOps practices. I focus on cloud infrastructure provisioning, IAM security automation, GitOps deployment models, platform availability, and efficient deployment automation across enterprise environments.",
    "achievements": [
        "Worked on AWS Identity and Access Management transformation for a leading mutual fund client, implementing policy controls and security automation using Open Policy Agent (OPA) with Rego.",
        "Supported AWS EKS environments by troubleshooting P1-P4 production issues and maintaining high availability for critical applications across multiple environments.",
        "Enabled GitOps-based delivery using ArgoCD and Helm for nearly 20 microservices and application workloads running in Kubernetes clusters.",
        "Designed and deployed cloud infrastructure on AWS using ECS, Lambda, S3, and CodeBuild, improving application delivery and operational efficiency.",
        "Improved engineering productivity through automation, CI/CD pipeline integration, and AI-assisted development workflows using GitHub Copilot."
    ],
    "experience": [
        {
            "domain": "AWS IAM & Security Automation",
            "years": "2024",
            "detail": "Led IAM transformation work for a mutual fund client by building access control rules, enforcing compliant policies, and integrating OPA checks into CI/CD pipelines to block non-compliant changes before deployment."
        },
        {
            "domain": "Kubernetes Operations & GitOps",
            "years": "2025",
            "detail": "Managed AWS EKS environments, handled production incidents, supported large application portfolios, and standardized deployment strategies using ArgoCD, Helm, Terraform, Jenkins, and GitHub-based workflows."
        },
        {
            "domain": "Cloud Platform Engineering",
            "years": "2026 - Present",
            "detail": "Designed and deployed AWS platform services like ECS, Lambda, S3, and CodeBuild while defining IAM roles, automating infrastructure using CloudFormation templates, and supporting cloud architecture decisions for scalable service delivery."
        }
    ],
    "projects": [
        {
            "name": "IAM Transformation Program",
            "description": "Executed an IAM modernization initiative for a large financial client, introducing access control policies and security guardrails through OPA Rego definitions. The project helped enforce least-privilege access and reduce risk by validating security compliance in development pipelines before code reached deployment stages."
        },
        {
            "name": "McDAM_BAS_K8DevOpsTool",
            "description": "Supported a large AWS EKS implementation with production-grade monitoring and issue resolution for critical workloads. The work included deployment support, platform reliability improvements, GitOps pipeline enablement, and coordination across engineering teams to maintain service continuity and operational stability."
        },
        {
            "name": "AWS Cloud Deployment Automation",
            "description": "Built and refined cloud deployment automation using CloudFormation, BAT scripts, ECS, Lambda, and S3 resources to streamline provisioning and application rollout. This effort improved deployment repeatability, reduced manual errors, and accelerated delivery across environments."
        },
        {
            "name": "Platform CI/CD Enablement",
            "description": "Enhanced the software delivery lifecycle by integrating GitHub, Jenkins, Docker, Terraform, and cloud-native tooling into standard workflows. The objective was to automate release validation, improve change confidence, and support a scalable DevOps culture in cloud engineering teams."
        }
    ],
    "certificates": [
        "Google Associate Cloud Engineer Certification",
        "HashiCorp Certified: Terraform Associate",
        "Microsoft Certified: Azure Developer Associate",
        "AWS Fundamentals: Building Serverless Applications",
        "Capgemini OCEAN Certified L1 - Cloud Platform Engineer - Cloud Fundamentals",
        "Capgemini OCEAN Certified L1 - Cloud Platform Engineer - DevSecOps",
        "Microsoft Azure Fundamentals (AZ-900)",
        "Agile Software Development"
    ]
}


@app.route("/")
def home():
    return render_template("index.html", data=portfolio)


@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
