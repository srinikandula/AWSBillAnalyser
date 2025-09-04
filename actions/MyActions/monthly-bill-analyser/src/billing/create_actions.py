from datetime import datetime, timedelta
from decimal import Decimal
from typing import List
from sema4ai.actions import ActionError, Response, action

from .models import CostAnalysisRequest, OptimizationOpportunity


@action(is_consequential=False)
def identify_cost_optimization_opportunities(
    cost_analysis_request: CostAnalysisRequest
) -> Response[List[OptimizationOpportunity]]:
    """
    Identifies cost optimization opportunities based on AWS usage patterns.

    Args:
        cost_analysis_request: Request containing billing period and filters.

    Returns:
        A list of optimization opportunities with potential savings.
    """
    # Simulate optimization analysis
    opportunities = [
        OptimizationOpportunity(
            service_name="Amazon EC2",
            resource_id="i-0123456789abcdef0",
            opportunity_type="rightsizing",
            current_cost=Decimal("450.00"),
            potential_savings=Decimal("180.00"),
            recommendation="Downsize from m5.xlarge to m5.large - CPU utilization consistently below 25%",
            effort_level="low"
        ),
        OptimizationOpportunity(
            service_name="Amazon RDS",
            resource_id="mydb-instance-1",
            opportunity_type="unused",
            current_cost=Decimal("320.00"),
            potential_savings=Decimal("320.00"),
            recommendation="Remove unused RDS instance that has had zero connections for 30+ days",
            effort_level="medium"
        ),
        OptimizationOpportunity(
            service_name="Amazon EC2",
            resource_id="i-0987654321fedcba0",
            opportunity_type="reserved_instance",
            current_cost=Decimal("800.00"),
            potential_savings=Decimal("240.00"),
            recommendation="Purchase 1-year Reserved Instance for consistent workload running 24/7",
            effort_level="low"
        ),
        OptimizationOpportunity(
            service_name="Amazon S3",
            resource_id="my-bucket-logs",
            opportunity_type="storage_class",
            current_cost=Decimal("150.00"),
            potential_savings=Decimal("90.00"),
            recommendation="Move infrequently accessed logs to S3 Intelligent-Tiering",
            effort_level="low"
        )
    ]
    
    # Apply filters if provided
    if cost_analysis_request.services_filter:
        opportunities = [opp for opp in opportunities 
                        if any(service in opp.service_name for service in cost_analysis_request.services_filter)]
    
    # Sort by potential savings (highest first)
    opportunities.sort(key=lambda x: x.potential_savings, reverse=True)
    
    total_potential_savings = sum(opp.potential_savings for opp in opportunities)
    print(f"Found {len(opportunities)} optimization opportunities with total potential savings of ${total_potential_savings}")
    
    return Response(result=opportunities)


@action(is_consequential=False)
def generate_cost_forecast(
    months_ahead: int = 3
) -> Response[dict]:
    """
    Generates a cost forecast based on historical trends.

    Args:
        months_ahead: Number of months to forecast (1-12).

    Returns:
        Cost forecast with projected monthly costs.
    """
    if months_ahead < 1 or months_ahead > 12:
        raise ActionError("Forecast period must be between 1 and 12 months")
    
    # Simulate forecast based on current trends
    base_cost = 1775.95
    growth_rate = 0.05  # 5% monthly growth
    
    forecast = {
        "forecast_period": f"{months_ahead} months",
        "base_monthly_cost": base_cost,
        "projected_growth_rate": f"{growth_rate * 100:.1f}%",
        "monthly_projections": []
    }
    
    for month in range(1, months_ahead + 1):
        projected_cost = base_cost * (1 + growth_rate) ** month
        forecast_date = (datetime.now() + timedelta(days=30 * month)).strftime("%Y-%m")
        
        forecast["monthly_projections"].append({
            "month": forecast_date,
            "projected_cost": round(projected_cost, 2),
            "cost_increase": round(projected_cost - base_cost, 2)
        })
    
    total_forecast_cost = sum(proj["projected_cost"] for proj in forecast["monthly_projections"])
    forecast["total_forecast_cost"] = round(total_forecast_cost, 2)
    
    print(f"Generated {months_ahead}-month cost forecast: ${forecast['total_forecast_cost']} total projected")
    
    return Response(result=forecast)
