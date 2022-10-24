# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

_For **both** a VM or App Service solution for the CMS app:_

- _Analyze costs, scalability, availability, and workflow_
- Cost wise VMs (IaaS) is more expinsive than App Service choice (Paas), but worth to mention that VMs are higher in scalability , and client can have more controll on his environemt , also it supports almost all languages and technologies to be hosted on.
- While VMs are the better choice for Big contious growth projects , App Service might be the better choice for small projects as well as the organaizations that doesn't have a dedecated person to manitain the VMs, one cost downside is that you have to pay even if your app is not running and limitted in the specs.

- _Choose the appropriate solution (VM or App Service) for deploying the app_
  -Since we have a small application that doesn't require huge interaction with the end user , most of it will be reading only , no multible user roles assigned, I Choase App Services , in feauture if we got huge traffice and our application went viral then for sacalling we can create mutible App services and make them HA.
- _Justify your choice_
- easier choice to maintain and configure.
- suitable for starter Application.
- low in cost comaring with VMs.

### Assess app changes that would change your decision.

_Detail how the app and any other needs would have to change for you to change your decision in the last section._
I would choose VMs:

- If new features Added that requires Contious User interaction which would bring a lot of traffic or if planning to go commercial.
- When Region IS comblinces is required for Infrasturucture.
- If I am migrating from on-premisses to Cloud and want more control over my environment.
