from typing import List
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime, timedelta
from models import Subscription, fake_subscriptions_db
from auth import verify_token

router = APIRouter()

@router.post("/subscriptions/", response_model=Subscription)
async def create_subscription(subscription: Subscription, token: str = Depends(verify_token)):
    subscription.start_date = datetime.utcnow()
    subscription.end_date = subscription.start_date + timedelta(days=30)
    subscription.active = True
    fake_subscriptions_db.append(subscription.dict())
    return subscription

@router.get("/subscriptions/{user_id}", response_model=List[Subscription])
async def get_user_subscriptions(user_id: str, token: str = Depends(verify_token)):
    user_subs = [sub for sub in fake_subscriptions_db if sub['user_id'] == user_id]
    if not user_subs:
        raise HTTPException(status_code=404, detail="No subscriptions found")
    return user_subs
