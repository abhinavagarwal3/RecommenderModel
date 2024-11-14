from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from supabase_client import supabase  # Import the configured Supabase client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Set to ["https://your-frontend-domain.com"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RecommendationRequest(BaseModel):
    user_id: str


@app.get("/")
async def root():
    return {"message": "Welcome to the Recommendation API!"}


@app.post("/recommendations")
async def get_recommendations(request: RecommendationRequest):
    user_id = request.user_id

    try:
        # Step 1: Fetch liked properties from the interactions table
        response = supabase.table("interactions").select("property_id").eq(
            "user_id", user_id).eq("interaction_type", "like").execute()
        liked_property_ids = [
            interaction["property_id"] for interaction in response.data
        ]

        # Step 2: Fetch all properties from the properties table
        response = supabase.table("properties").select("*").execute()
        all_properties = response.data

        # Step 3: Generate recommendations
        recommended_properties = [
            property for property in all_properties
            if property["id"] in liked_property_ids
        ]

        return {"recommended_properties": recommended_properties}

    except Exception as e:
        print(f"Error in recommendation API: {e}")
        raise HTTPException(status_code=500,
                            detail="Failed to generate recommendations")
