"""
AWS Billing Analysis Actions

Provides functionality to analyze AWS costs and usage data.
"""

import json
from datetime import datetime, timedelta
from decimal import Decimal
from typing import List, Dict, Any
from sema4ai.actions import ActionError, Response, action

from .models import CostAnalysisRequest, CostSummary, AWSService, BillingPeriod


@action(is_consequential=False)
def analyze_cost_trends(
    cost_analysis_request: CostAnalysisRequest
) -> Response[CostSummary]:
    """
    Analyzes AWS cost trends for a given billing period.

    Args:
        cost_analysis_request: Request containing billing period and filters.

    Returns:
        A comprehensive cost analysis summary.
    """
    # Simulate cost analysis (in real implementation, this would connect to AWS Cost Explorer API)
    mock_services = [
        AWSService(
            service_name="Amazon EC2",
            region="us-east-1",
            cost=Decimal("1250.45"),
            usage_quantity=Decimal("744"),
            usage_unit="Hrs"
        ),
        AWSService(
            service_name="Amazon RDS",
            region="us-east-1",
            cost=Decimal("450.30"),
            usage_quantity=Decimal("744"),
            usage_unit="Hrs"
        ),
        AWSService(
            service_name="Amazon S3",
            region="us-east-1",
            cost=Decimal("75.20"),
            usage_quantity=Decimal("500"),
            usage_unit="GB"
        )
    ]
    
    # Apply filters if provided
    if cost_analysis_request.services_filter:
        mock_services = [s for s in mock_services if s.service_name in cost_analysis_request.services_filter]
    
    if cost_analysis_request.cost_threshold:
        mock_services = [s for s in mock_services if s.cost >= cost_analysis_request.cost_threshold]
    
    total_cost = sum(service.cost for service in mock_services)
    
    cost_summary = CostSummary(
        total_cost=total_cost,
        previous_period_cost=Decimal("1650.25"),
        cost_change_percent=Decimal("8.5"),
        top_services=sorted(mock_services, key=lambda x: x.cost, reverse=True)[:5],
        cost_by_region=[
            {"region": "us-east-1", "cost": float(total_cost)},
            {"region": "us-west-2", "cost": 125.50}
        ]
    )
    
    print(f"Analyzed costs for period {cost_analysis_request.billing_period.start_date} to {cost_analysis_request.billing_period.end_date}")
    print(f"Total cost: ${total_cost}")
    
    return Response(result=cost_summary)


@action(is_consequential=False)
def get_monthly_cost_breakdown(
    year: int, month: int
) -> Response[Dict[str, Any]]:
    """
    Gets a detailed cost breakdown for a specific month.

    Args:
        year: Year for the cost analysis.
        month: Month for the cost analysis (1-12).

    Returns:
        Monthly cost breakdown by service and region.
    """
    if month < 1 or month > 12:
        raise ActionError("Month must be between 1 and 12")
    
    if year < 2020 or year > datetime.now().year:
        raise ActionError(f"Year must be between 2020 and {datetime.now().year}")
    
    # Simulate monthly breakdown
    breakdown = {
        "month": f"{year}-{month:02d}",
        "total_cost": 1775.95,
        "services": [
            {"name": "Amazon EC2", "cost": 1250.45, "percentage": 70.4},
            {"name": "Amazon RDS", "cost": 450.30, "percentage": 25.4},
            {"name": "Amazon S3", "cost": 75.20, "percentage": 4.2}
        ],
        "regions": [
            {"name": "us-east-1", "cost": 1650.45, "percentage": 92.9},
            {"name": "us-west-2", "cost": 125.50, "percentage": 7.1}
        ],
        "cost_categories": [
            {"name": "Compute", "cost": 1250.45, "percentage": 70.4},
            {"name": "Storage", "cost": 525.50, "percentage": 29.6}
        ]
    }
    
    print(f"Monthly breakdown for {year}-{month:02d}: ${breakdown['total_cost']}")
    
    return Response(result=breakdown)
