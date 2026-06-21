markdown# HumanGov Application

A simulated U.S. Department of Education web application used as the foundation for a hands-on cloud infrastructure and DevOps migration project. This repository contains the application code; infrastructure code lives in [human-gov-infrastructure](https://github.com/grbyrd99/human-gov-infrastructure).

## Project Overview

HumanGov is a multi-tenant SaaS application designed to manage human resources data for state government agencies. The application was originally deployed on a single EC2 instance and has been progressively migrated to a modern containerized architecture on AWS as requirements from the simulated CIO evolved over time.

This project demonstrates real-world infrastructure decision-making — each migration phase was driven by a specific requirement: scalability, isolation, resilience, or cost optimization.

## Architecture Evolution

| Phase | Infrastructure | Status |
|-------|----------------|--------|
| 1 | EC2 — single instance deployment | Complete |
| 2 | Dockerized application | Complete |
| 3 | AWS ECS + ECR + ALB — multi-tenant, siloed by state | Complete |
| 4 | AWS EKS — Kubernetes orchestration | In Progress |

## Current Architecture (Phase 3)

The application runs on **Amazon ECS (Elastic Container Service)** fronted by an **Application Load Balancer (ALB)**, with Docker images stored in **Amazon ECR (Elastic Container Registry)**. Each state tenant (Florida, California, etc.) is isolated with its own ECS service, DynamoDB table, and S3 bucket.
GitHub Actions → Docker Build → ECR → ECS (per-tenant) → ALB

↓

DynamoDB + S3 (per-tenant)

### AWS Services Used

- Amazon ECS (Fargate)
- Amazon ECR
- Application Load Balancer (ALB)
- Amazon DynamoDB (per-tenant)
- Amazon S3 (per-tenant)
- VPC, Subnets, Security Groups
- GitHub Actions (CI/CD)

## Tech Stack

- **Application:** Python, HTML
- **Containerization:** Docker
- **Cloud:** AWS
- **Infrastructure as Code:** Terraform (see [human-gov-infrastructure](https://github.com/grbyrd99/human-gov-infrastructure))

## About This Project

This project is part of a hands-on DevOps and cloud engineering bootcamp. It is designed to simulate the kind of incremental infrastructure evolution a cloud engineer encounters in enterprise environments — receiving requirements, evaluating options, and implementing changes without disrupting existing tenants.

> **Note:** The Flask application code was provided as part of the bootcamp curriculum. Infrastructure design, provisioning, containerization, and all AWS deployment work was performed by Gary Byrd.Claude responded: The rest of the README looks great — headers, bullets, all rendering correctly.Thought processThought processThe rest of the README looks great — headers, bullets, all rendering correctly. The only problem is the table. GitHub is not recognizing the separator row.
Go into edit mode and find the Infrastructure Evolution table. Replace just that section with this simpler format — single dashes instead of long dashes in the separator row:
| Phase | What Was Built | Status |
| --- | --- | --- |
| 1 | EC2 instance, VPC, Security Groups | Complete |
| 2 | Docker containerization, ECR repository | Complete |
| 3 | ECS Cluster, ALB, per-tenant DynamoDB and S3, multi-tenant isolation | Complete |
| 4 | EKS cluster, Kubernetes workloads | In Progress |
That's it — just swap out that one section. Everything else can stay as-is. The same fix applies to the application repo table when you get to that one.Claude Fable 5 is currently unavailable.Learn more(opens in new tab)
AskSonnet 4.6Claude is AI and can make mistakes. Please double-check responses. Give us feedbackHuman gov infrastructure readme · MDGoogle DriveHumanGov Infrastructure

Terraform infrastructure-as-code for the HumanGov application — a simulated multi-tenant SaaS platform for U.S. state government agencies running on AWS.

Overview

This repository manages all AWS infrastructure for the HumanGov application using Terraform. Infrastructure is provisioned as code to ensure consistency, repeatability, and auditability across environments. Each migration phase introduces new infrastructure components in response to requirements from the simulated CIO.

Infrastructure Evolution

PhaseWhat Was BuiltStatus1EC2 instance, VPC, Security GroupsComplete2Docker containerization, ECR repositoryComplete3ECS Cluster, ALB, per-tenant DynamoDB and S3, multi-tenant isolationComplete4EKS cluster, Kubernetes workloadsIn Progress

Current Infrastructure (Phase 3)

Multi-Tenant Architecture

Each state tenant is provisioned with isolated AWS resources to ensure data separation and independent scalability:


Amazon ECS — containerized application per tenant
Amazon ECR — Docker image registry
Application Load Balancer — routes traffic to tenant-specific ECS services
Amazon DynamoDB — per-tenant data store
Amazon S3 — per-tenant object storage
VPC — isolated network with public/private subnets, security groups


Terraform Structure

terraform/
├── main.tf          # Core infrastructure resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
└── ...

Technologies


IaC: Terraform (HCL)
Cloud Provider: AWS
Services: ECS, ECR, ALB, DynamoDB, S3, VPC, IAM


Usage

bash# Initialize Terraform
terraform init

# Preview changes
terraform plan

# Apply infrastructure
terraform apply

# Destroy infrastructure
terraform destroy

Related Repository

Application code: grbyrd99/human-gov-application

About This Project

Part of a hands-on DevOps and cloud engineering bootcamp simulating enterprise infrastructure evolution. Each phase is driven by a new CIO requirement, mirroring real-world cloud engineering engagements where infrastructure must evolve incrementally without disrupting existing workloads.
ProgressSee task progress for longer tasks.ResumesInstructions · CLAUDE.mdGaryByrd_CloudEngineer_General_v13.docxGaryByrd_CloudEngineer_General_v12.docxGaryByrd_CloudEngineer_General.docxGaryByrd_Microsoft_SolutionEngineer.docxGaryByrd_Parsons_SrCloudAutomationEngineer.docxGaryByrd_RobertHalf_CloudEngineer.docxGaryByrd_Amatriot_AzureCloudPlatformEngineer.docxGaryByrd_Amatriot_AzureCloudPlatformEngineer_CoverLetter.docxGaryByrd_Electrosoft_SecurityEngineer.docxGaryByrd_Electrosoft_SecurityEngineer_CoverLetter.docxGaryByrd_StealthTalent_SrITSystemsEngineer.docxGaryByrd_PrecisionMedicine_SrITEngineer.docxGaryByrd_IntegraConnect_SrITEngineer.docxGaryByrd_Amatriot_CoverLetter.docxGaryByrd_Conviso_IdentityEndpointEngineer.docxGaryByrd_BBraun_InfraCloudSpecialist.docxGaryByrd_GDIT_AzureCloudEngineer.docxGaryByrd_AzureArchitect_Contract.docxGaryByrd_Cyclotron_AzureEngineer.docxGaryByrdDevOps.docxGaryByrd_NewEra_SrAzureInfraEngineer.docxGaryByrd_Conviso_AzureInfraSpecialist.docxGaryByrd_Highmark_SrCloudEngineer.docxGaryByrd_enGen_SrCloudEngineer.docxGaryByrd_InterviewCheatSheet.mdGaryByrd_Infosys_AzureSecurityEngineer.docxGaryByrd_Infosys_InterviewPrep.mdGaryByrd_BBraun_CoverLetter.docxGaryByrd_BHGFinancial_InfraCloudEngineer.docxGaryByrd_LSEG_ActiveDirectoryEngineer.docxGaryByrd_ConsciousNetworks_M365SecurityEngineer.docxGaryByrd_SysAdmin_EnterpriseInfra.docxGaryByrd_Rezilient_SrITEngineer.docxGaryByrd_FCSFinancial_DevOpsEngineer.docxGaryByrd_TSA_M365PlatformEngineer.docxGaryByrd_HealthcareIT_DirectorIT.docxGARY BYRD--Resume.docxGary Byrd_Cloud Engineer.docxGaryByrd_LinuxBackground.mdOutputshuman-gov-application-README.mdhuman-gov-infrastructure-README.mdGaryByrd_VeritaAI_CybersecuritySpecialist.docxbuild_resume.jspackage-lock.jsonpackage.jsondocument.xmlGaryByrd_CloudEngineer_General.docxGaryByrd_CloudEngineer_General_v2.docxGaryByrd_CloudEngineer_General_v3.docxGaryByrd_CloudEngineer_General_v4.docxGaryByrd_CloudEngineer_General_v5.docxGaryByrd_CloudEngineer_General_v6.docxGaryByrd_CloudEngineer_General_v7.docxGaryByrd_CloudEngineer_General_v8.docxGaryByrd_CloudEngineer_General_v9.docxGaryByrd_CloudEngineer_General_v10.docxGaryByrd_CloudEngineer_General_v11.docxScratchpadContext
