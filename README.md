# Python Training Hub 2.0
A Comprehensive Beginner-Friendly Python Curriculum

## Overview

Python Learning Hub is a standalone, browser-compatible educational platform designed to teach Python programming to complete beginners. Each lesson is a self-contained HTML file that renders perfectly in both standard web browsers and Atlassian Confluence (via the HTML macro), eliminating the need for separate course platforms.

## Project Goals

- **Break down complex concepts** into clear, digestible lessons with analogies and real-world examples
- **Build confidence** through structured progressive learning: objectives → overview → key ideas → code examples → practice exercises → knowledge checks
- **Support multiple learning styles** with text explanations, visual components (icons, gradients, cards), live code examples, and interactive quizzes
- **Ensure accessibility** across platforms—lessons work equally well in a browser tab or embedded inside Confluence documentation

## Structure

Lessons are organized by **track** and **module**:
```
pages/
├── track_01/
│   ├── mod_01_getting_started/
│   │   ├── lesson01.html
│   │   ├── lesson02.html
│   │   └── ...
│   └── mod_02_[next_topic]/
```

Every lesson follows the same proven structure:
1. **Objectives** – learning goals in a 4-card grid
2. **Overview** – hook quote + real-world analogy
3. **Key Ideas** – takeaways with visual emphasis
4. **Key Concepts** – detailed sidebars with code examples
5. **Code Examples** – standalone working scripts with integrated terminals
6. **Practice Exercises** – hands-on coding tasks
7. **Knowledge Check** – interactive quiz
8. **Next Lesson** – preview and navigation

## Design System

Built on **Tailwind CSS** with a custom brand identity:
- **Primary Color:** `#CB187D` (brand pink) with gradient to `#e84aad`
- **Typography:** Inter (body) + Fira Code (code blocks)
- **Components:** Tab systems, accordions, code blocks with copy buttons, quiz feedback, scroll progress indicator, and back-to-top navigation

## Confluence-Ready Architecture

Lessons are **not** standalone HTML documents with `<!DOCTYPE>` or `<html>` tags—they're HTML fragments designed to be pasted directly into Confluence. A `#hub-root` CSS isolation block ensures all styles survive Confluence's aggressive HTML sanitizer, so learners get the same polished experience whether they're viewing the lesson in a browser or embedded in documentation.

## Key Features

- ✅ **No build process** – CDN-based dependencies (Tailwind, Prism.js, Iconify, Google Fonts)
- ✅ **Copy-to-clipboard code blocks** – learners can instantly grab code to try themselves
- ✅ **Mobile responsive** – TOC sidebar hides on small screens, content reflows gracefully
- ✅ **Syntax highlighting** – Python, Bash, and SQL code with Prism.js
- ✅ **Interactive tabs** – switch between code examples, mistakes, exercises, and quiz questions without page reload
- ✅ **Scroll progress bar** – visual feedback on lesson progress
- ✅ **Accessibility-first writing** – plain English explanations, complete sentences, no jargon without definition

## Getting Started

1. Clone the repository
2. Open any lesson file in your browser
3. To embed in Confluence, copy the entire file contents and paste into the HTML macro

See `docs/new_lesson_template.html` for the master template—all new lessons clone this file and customize the content.
