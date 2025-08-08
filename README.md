Candidate Recommendation Engine

This project is a Streamlit-based application that helps match candidate resumes to a given job description by using semantic similarity. It works with both PDF and text resumes, extracting the content, generating embeddings with the all-MiniLM-L6-v2 model from sentence-transformers, and then calculating cosine similarity scores to rank candidates in order of relevance. The app also integrates the OpenAI API to generate a concise fit analysis for each candidate, including a short summary and a list of pros and cons based on the resume content.

The process begins by converting both the job description and the resumes into vector embeddings, ensuring that the comparison is based on meaning rather than simple keyword matching. Similarity scores are calculated with scikit-learn’s cosine similarity, and the results are sorted so that the most relevant candidates appear at the top. For each candidate, the app uses GPT-3.5 to produce a short explanation of why the person is a good match and highlights their strengths and weaknesses in relation to the role.

The interface is built with Streamlit, making it easy to upload multiple resumes, view similarity scores, read AI-generated summaries, and preview resume content directly in the browser. The application assumes that resumes contain extractable text, meaning that scanned images without OCR will not work. It also assumes that the OpenAI API key is provided securely as an environment variable or through Streamlit Cloud’s secrets management.

For local use, the repository includes a requirements.txt file listing all dependencies, and setup is as simple as creating a Python environment, installing the packages, setting the OPENAI_API_KEY, and running the app with streamlit run. Deployment to Streamlit Cloud is straightforward — push the code to GitHub, link the repository in Streamlit, set the API key in the secrets manager, and launch the app.


Link : https://candidate-recommendation-engine-7cgjh7eprtvjzngwe6bk2j.streamlit.app/
