from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# Model parameters
PARAMETERS = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
}

# watsonx credentials
# Note: Normally we'd need an API key, but in Skill's Network Cloud IDE will automatically handle that for you.
credentials = Credentials(
                   url = "https://us-south.ml.cloud.ibm.com",
                   api_key = "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" 
                  )

# Model IDs
LLAMA3_MODEL_ID = "meta-llama/llama-3-2-11b-vision-instruct"
GRANITE_MODEL_ID = "ibm/granite-3-8b-instruct"
MIXTRAL_MODEL_ID = "mistralai/mistral-large"
