from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field


class BillingPeriod(BaseModel):
    start_date: datetime = Field(description="Start date of the billing period")
    end_date: datetime = Field(description="End date of the billing period")


class AWSService(BaseModel):
    service_name: str = Field(description="Name of the AWS service")
    region: str = Field(description="AWS region")
    cost: Decimal = Field(description="Cost for this service")
    usage_quantity: Optional[Decimal] = Field(default=None, description="Usage quantity")
    usage_unit: Optional[str] = Field(default=None, description="Unit of usage measurement")


class CostAnalysisRequest(BaseModel):
    billing_period: BillingPeriod = Field(description="Billing period to analyze")
    services_filter: Optional[List[str]] = Field(default=None, description="Filter by specific services")
    regions_filter: Optional[List[str]] = Field(default=None, description="Filter by specific regions")
    cost_threshold: Optional[Decimal] = Field(default=None, description="Only show costs above this threshold")


class OptimizationOpportunity(BaseModel):
    service_name: str = Field(description="AWS service with optimization opportunity")
    resource_id: Optional[str] = Field(default=None, description="Resource identifier")
    opportunity_type: str = Field(description="Type of optimization (rightsizing, unused, reserved_instance)")
    current_cost: Decimal = Field(description="Current monthly cost")
    potential_savings: Decimal = Field(description="Potential monthly savings")
    recommendation: str = Field(description="Specific recommendation")
    effort_level: str = Field(description="Implementation effort (low, medium, high)")


class CostSummary(BaseModel):
    total_cost: Decimal = Field(description="Total cost for the period")
    previous_period_cost: Optional[Decimal] = Field(default=None, description="Cost for previous period")
    cost_change_percent: Optional[Decimal] = Field(default=None, description="Percentage change from previous period")
    top_services: List[AWSService] = Field(description="Top services by cost")
    cost_by_region: List[dict] = Field(description="Cost breakdown by region")
