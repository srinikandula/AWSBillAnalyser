# AWS Bill Analyser Actions

This action package provides comprehensive AWS billing analysis capabilities for the AWSBillAnalyser Sema4.ai agent. It enables detailed cost analysis, optimization recommendations, and forecasting for AWS infrastructure.

## Features

### Cost Analysis
- **Trend Analysis**: Analyze AWS costs over custom time periods with filtering by services, regions, and cost thresholds
- **Monthly Breakdowns**: Get detailed cost breakdowns by service, region, and cost categories
- **Period Comparisons**: Compare costs across different billing periods with percentage changes

### Cost Optimization
- **Optimization Opportunities**: Identify specific cost-saving opportunities including:
  - EC2 rightsizing recommendations
  - Unused resource identification
  - Reserved Instance opportunities
  - Storage class optimization
- **Savings Estimation**: Calculate potential monthly savings with implementation effort levels
- **Prioritized Recommendations**: Sort opportunities by potential savings impact

### Forecasting
- **Cost Projections**: Generate 1-12 month cost forecasts based on historical trends
- **Growth Rate Analysis**: Project costs with configurable growth rates
- **Budget Planning**: Support for budget planning with projected total costs

## Actions

### `analyze_cost_trends(cost_analysis_request)`
Analyzes AWS cost trends for a given billing period with optional filtering.

**Parameters:**
- `cost_analysis_request`: CostAnalysisRequest containing billing period and filters

**Returns:** CostSummary with total costs, trends, and service breakdowns

### `get_monthly_cost_breakdown(year, month)`
Provides detailed monthly cost breakdown by service and region.

**Parameters:**
- `year`: Year for analysis (2020-current)
- `month`: Month for analysis (1-12)

**Returns:** Monthly breakdown with service, region, and category costs

### `identify_cost_optimization_opportunities(cost_analysis_request)`
Identifies specific cost optimization opportunities with savings estimates.

**Parameters:**
- `cost_analysis_request`: CostAnalysisRequest for filtering opportunities

**Returns:** List of OptimizationOpportunity objects with recommendations and savings

### `generate_cost_forecast(months_ahead)`
Generates cost forecasts based on historical trends.

**Parameters:**
- `months_ahead`: Number of months to forecast (1-12)

**Returns:** Cost forecast with monthly projections and growth analysis

## Data Models

The action package uses sophisticated Pydantic models for AWS billing data:

- **BillingPeriod**: Date ranges for analysis periods
- **AWSService**: Service-specific cost and usage data
- **CostAnalysisRequest**: Analysis parameters with filtering options
- **OptimizationOpportunity**: Detailed optimization recommendations
- **CostSummary**: Comprehensive cost analysis results

## Development

### Testing
```bash
cd actions/MyActions/monthlybillanalyser
pytest
```

### Type Checking
```bash
mypy src tests
```

### Sample Data
The `devdata/` directory contains sample input files for testing the actions:
- `input_analyze_cost_trends.json`
- `input_get_monthly_cost_breakdown.json`

## Implementation Notes

- Uses `Decimal` for precise financial calculations
- Currently implements mock data for development/testing
- In production, would integrate with AWS Cost Explorer API
- Follows Sema4.ai Actions framework best practices
- Comprehensive error handling and validation

🚀 This action package leverages the full Python ecosystem for AWS billing analysis. Sema4.ai provides extensive [libraries](https://pypi.org/search/?q=robocorp-) for building powerful automation actions.

👉 Check [Action Server](https://github.com/Sema4AI/actions/tree/master/action_server/docs) and [Actions](https://github.com/Sema4AI/actions/tree/master/actions/docs) docs for more information.