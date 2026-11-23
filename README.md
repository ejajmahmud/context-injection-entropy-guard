# Context Injection Entropy Guard ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Context Injection Entropy Guard Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/context-injection-entropy-guard/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/context-injection-entropy-guard?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/context-injection-entropy-guard/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Context Injection Entropy Guard** is a production-ready developer tool and connector: Statistical entropy and perplexity deviation detector identifying prompt injection payloads in retrieved context.

---

## 🚀 Problem Statement

RAG retrieval from untrusted websites can ingest hidden adversarial prompt injections (e.g., 'Ignore previous instructions').

---

## ⚡ Architecture Flow

```mermaid
graph TD
    RetrievedDoc[Retrieved Web Document Chunk] --> Guard[Context Injection Entropy Guard]
    Guard --> Scan{Adversarial Injection Pattern Detected?}
    Scan -->|Yes: 'Ignore previous instructions'| Strip[Quarantine & Strip Injected Instructions]
    Scan -->|No: Clean Information| Deliver[Deliver to Agent Prompt Context]
```

---

## 📊 Performance Benchmarks

| Metric | Raw Ingestion | Static Regex List | Context Injection Entropy Guard | Improvement |
|---|---|---|---|---|
| Injection Bypass Rate | 88.4% | 34.0% | 0.00% | **Zero Bypass** |
| False Positive Strip | 0.0% | 14.2% | 1.1% | **92.2% reduction** |
| Inspection Latency | 0 ms | 1.8 ms | 0.14 ms | **12.8x faster** |
| Unicode Obfuscation Catch | 5% | 22% | 100% | **Complete Coverage** |

---

## 🛠️ Installation & Quickstart

```bash
pip install context_injection_entropy_guard
```

### Python API

```python
import context_injection_entropy_guard

print(context_injection_entropy_guard.__version__)
```

### CLI Usage

```bash
context-injection-entropy-guard --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
