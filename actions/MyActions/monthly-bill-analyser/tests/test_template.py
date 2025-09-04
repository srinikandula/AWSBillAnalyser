from datetime import datetime
from decimal import Decimal

def test_billing_actions() -> None:
    from billing.get_actions import analyze_cost_trends, get_monthly_cost_breakdown  # noqa
    from billing.create_actions import identify_cost_optimization_opportunities, generate_cost_forecast  # noqa
    from billing.models import BillingPeriod, CostAnalysisRequest  # noqa

    # Test that actions can be imported without errors
    assert analyze_cost_trends is not None
    assert get_monthly_cost_breakdown is not None
    assert identify_cost_optimization_opportunities is not None
    assert generate_cost_forecast is not None

def test_billing_models() -> None:
    from billing.models import BillingPeriod, AWSService, CostAnalysisRequest, OptimizationOpportunity, CostSummary  # noqa
    
    # Test BillingPeriod model
    period = BillingPeriod(
        start_date=datetime(2024, 1, 1),
        end_date=datetime(2024, 1, 31)
    )
    assert period.start_date.year == 2024
    assert period.start_date.month == 1
    
    # Test AWSService model
    service = AWSService(
        service_name="Amazon EC2",
        region="us-east-1",
        cost=Decimal("100.50")
    )
    assert service.service_name == "Amazon EC2"
    assert service.cost == Decimal("100.50")
    
    # Test CostAnalysisRequest model
    request = CostAnalysisRequest(
        billing_period=period,
        services_filter=["Amazon EC2", "Amazon RDS"],
        cost_threshold=Decimal("50.00")
    )
    assert len(request.services_filter) == 2
    assert request.cost_threshold == Decimal("50.00")

def test_optimization_opportunity_model() -> None:
    from billing.models import OptimizationOpportunity  # noqa
    
    opportunity = OptimizationOpportunity(
        service_name="Amazon EC2",
        resource_id="i-123456789",
        opportunity_type="rightsizing",
        current_cost=Decimal("200.00"),
        potential_savings=Decimal("80.00"),
        recommendation="Downsize instance type",
        effort_level="low"
    )
    
    assert opportunity.service_name == "Amazon EC2"
    assert opportunity.potential_savings == Decimal("80.00")
    assert opportunity.effort_level == "low"
