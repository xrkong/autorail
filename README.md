# 🛡️ AutoRail 
The word '*AutoRail*' is **auto**Gen and guard**rail** combined. 
Make LLM's output more consistent with human values, using [AutoGen](https://github.com/microsoft/autogen) and [Guardrails](https://github.com/guardrails-ai/guardrails).

## 💡 What the project does
AutoRail is a proof of concept that utilizes AutoGen and Guardrails to align the output of LLMs with human values. It is a project that is still in progress. 
Our goal is to build a complete AI safety framework to evaluate and modify the output text of LLM so that its values align with those of *governments, political parties, and other organizations*.

## 🌟 Why the project is useful
This project provides a framework to score, evaluatr, and revise the output of LLM. 
We provide a framework and you provide the value documents of your organization. 
This [^1]

## 🚀 How users can get started with the project
This example can be run with
```bash
python autorail/autorail.py
```

## 📋 Framework details

![AutoRail Overview](doc/images/autorail_overview.png)  

## 📍 Roadmap
- [x] Create a proof of concept
- [x] AutoRail group chat
- [x] Log messages and token cost
- [ ] Convert guardrails to system prompt
- [ ] Azure deployment
- [ ] Write framework details 
- [ ] Write tutorials
- [ ] Package it as a library
<!-- 
- [ ] Write a paper 
- [ ] Cite reference
-->

## 🛠️ Contributing
Get started by checking out Github issues and of course using Guardrails to familiarize yourself with the project.
We encourage users to provide **public** value documents.
Convert your value documents into a format that can be used by guardrails. 

## references
[^1]: Wu, Q., Bansal, G., Zhang, J., Wu, Y., Zhang, S., Zhu, E., ... & Wang, C. (2023). Autogen: Enabling next-gen llm applications via multi-agent conversation framework. arXiv preprint arXiv:2308.08155. [](https://arxiv.org/abs/2308.08155)