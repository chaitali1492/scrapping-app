import re
from mognodb import insertEmbedding
from utils import getEmbeddings

def read_and_chunk_text(file_path, sentences_per_chunk=10):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Merge into a single line (remove newlines)
    text = text.replace('\n', ' ').replace('\r', ' ')
    
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Split text into sentences using a regex pattern for sentence endings
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    # Group sentences into chunks of specified size
    chunks = []
    for i in range(0, len(sentences), sentences_per_chunk):
        chunk = ' '.join(sentences[i:i+sentences_per_chunk])
        chunks.append(chunk)
    
    return chunks


file_path = 'full_website_content-2.txt'
chunks = read_and_chunk_text(file_path, sentences_per_chunk=30)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    print('-----')
    embedding = getEmbeddings(chunk)
    data = {'content': chunk, 'embedding': embedding}
    insertEmbedding(data)

print("done with insert")
