# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.1.3] - YYYY-MM-DD

### Bug fixes
- Fix demo scaffolding
- deps: bump postcss from 8.2.3 to 8.2.4
- Add correct badges in demo

### Tests
- Add tests for demo scaffolding

### Build System
- Remove GitHub workflow duplication on PR
- Fix coverage upload by switching to codecov

## [3.1.2] - 2021-01-14

### Bug fixes
- Fix typo in demo dependencies

### Build System
- Add auto-updates of dependencies via dependabot
- Improve version bumping workflow

## [3.1.1] - 2021-01-09

### Bug fixes
- Fix demo scaffolding issues when running `npm install`

## [3.1.0] - 2021-01-09

### Features
- Update demo to use Vue 3.0
- Running python craft inertia:demo scaffold a demo into your project (#3)

## [3.0.0a1] - 2021-01-08

### Features
- Add support for Masonite 3.0. If you want to use masonite-inertia with Masonite 2.X please use v2.X version.