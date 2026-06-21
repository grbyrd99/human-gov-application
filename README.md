Thought process
Thought process
Same problem here — the table is broken, and the bullet lists and bold text in "AWS Services Used" and "Tech Stack" are also running together. The content is all there, it's just the formatting that didn't survive the paste.

Replace the entire application README with this:

markdown
# HumanGov Application

A simulated U.S. Department of Education web application used as the foundation for a hands-on cloud infrastructure and DevOps migration project. This repository contains the application code; infrastructure code lives in [human-gov-infrastructure](https://github.com/grbyrd99/human-gov-infrastructure).

## Project Overview

HumanGov is a multi-tenant SaaS application designed to manage human resources data for state government agencies. The application was originally deployed on a single EC2 instance and has been progressively migrated to a modern containerized architecture on AWS as requirements from the simulated CIO evolved over time.

This project demonstrates real-world infrastructure decision-making — each migration phase was driven by a specific requirement: scalability, isolation, resilience, or cost optimization.

## Architecture Evolution

|
 Phase 
|
 Infrastructure 
|
 Status 
|
|
---
|
---
|
---
|
|
 1 
|
 EC2 — single instance deployment 
|
 Complete 
|
|
 2 
|
 Dockerized application 
|
 Complete 
|
|
 3 
|
 AWS ECS + ECR + ALB — multi-tenant, siloed by state 
|
 Complete 
|
|
 4 
|
 AWS EKS — Kubernetes orchestration 
|
 In Progress 
|

## Current Architecture (Phase 3)

The application runs on **Amazon ECS (Elastic Container Service)** fronted by an **Application Load Balancer (ALB)**, with Docker images stored in **Amazon ECR (Elastic Container Registry)**. Each state tenant (Florida, California, etc.) is isolated with its own ECS service, DynamoDB table, and S3 bucket.

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

## Related Repository

Infrastructure provisioning for this application is managed separately using Terraform:
[grbyrd99/human-gov-infrastructure](https://github.com/grbyrd99/human-gov-infrastructure)

## About This Project

This project is part of a hands-on DevOps and cloud engineering bootcamp. It is designed to simulate the kind of incremental infrastructure evolution a cloud engineer encounters in enterprise environments — receiving requirements, evaluating options, and implementing changes without disrupting existing tenants.

> **Note:** The Flask application code was provided as part of the bootcamp curriculum. Infrastructure 
