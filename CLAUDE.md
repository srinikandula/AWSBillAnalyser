# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture Overview

This is a Sema4.ai AI Agent project for analyzing AWS billing data. The project is designed as an expert AWS billing analyst that helps users understand, analyze, and optimize their AWS costs:

- **Agent Definition**: Configured in `agent-spec.yaml` as "AWSBillAnalyser" using OpenAI GPT-4o model
- **Action Package**: Located in `actions/MyActions/monthlybillanalyser/` containing AWS billing analysis functionality
- **Expert Role**: Functions as an AWS billing analysis expert providing cost optimization recommendations

## Project Structure

```
AWSBillAnalyser/
├── agent-spec.yaml           # Agent configuration and metadata
├── runbook.md               # Comprehensive agent instructions and role definition
├── actions/MyActions/monthlybillanalyser/  # Main action package
    ├── src/billing/         # AWS billing analysis modules
    │   ├── get_actions.py   # Cost analysis and reporting actions
    │   ├── create_actions.py # Optimization and forecasting actions
    │   └── models.py        # AWS billing data models
    ├── tests/               # Test files for billing functionality
    ├── devdata/            # Sample input files for testing actions
    └── pyproject.toml       # Python project configuration
```

## Development Commands

### Testing
```bash
cd actions/MyActions/monthlybillanalyser
pytest
```

### Type Checking
```bash
cd actions/MyActions/monthlybillanalyser
mypy src tests
```

## Key Components

### AWS Billing Analysis Actions
- `analyze_cost_trends()`: Analyzes AWS cost trends for a billing period with filtering capabilities
- `get_monthly_cost_breakdown()`: Provides detailed monthly cost breakdowns by service and region
- `identify_cost_optimization_opportunities()`: Identifies cost optimization opportunities with savings potential
- `generate_cost_forecast()`: Creates cost forecasts based on historical trends

### Data Models
- `BillingPeriod`: Date range for billing analysis
- `AWSService`: AWS service cost and usage data
- `CostAnalysisRequest`: Request parameters for cost analysis with filters
- `OptimizationOpportunity`: Cost optimization recommendations with savings estimates
- `CostSummary`: Comprehensive cost analysis results

### Configuration
- Uses pytest with custom configuration for testing
- MyPy configured with strict type checking
- Action package excludes common development files (`.git`, `.vscode`, `venv`, etc.)
- Decimal precision for accurate financial calculations

## Agent Capabilities

The agent specializes in:
- **Cost Analysis**: Parse AWS billing data, identify trends, and compare time periods
- **Optimization Recommendations**: Suggest rightsizing, Reserved Instances, and unused resource cleanup
- **Forecasting**: Generate cost projections based on historical usage patterns
- **Reporting**: Create actionable cost summaries with specific dollar amounts and percentages

## Important Notes

- All cost calculations use Decimal precision for financial accuracy
- The agent treats billing information as sensitive and confidential
- Actions are currently implemented with mock data for development/testing
- In production, these would connect to AWS Cost Explorer API
- The agent operates in conversational mode providing expert AWS billing guidance