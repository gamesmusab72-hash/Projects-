# This is basically a recommendation system that I built using PyTorch. 
# It uses embeddings to learn user and show representations and predicts which shows a user might like based on their past interactions.
import torch
import torch.nn as nn
import torch.optim as optim

# Example data (user_id, show_id, watched=1)
# In practice, you'd load this from your dataset
interactions = [
    (0, 0, 1),  # user 0 watched show 0
    (0, 1, 1),  # user 0 watched show 1
    (1, 1, 1),  # user 1 watched show 1
    (1, 2, 1),  # user 1 watched show 2
]

# Parameters
num_users = 3   # total users
num_shows = 4   # total shows
embedding_dim = 8

# Model: user and show embeddings → dot product → prediction
class Recommender(nn.Module):
    def __init__(self, num_users, num_shows, embedding_dim):
        super().__init__()
        self.user_emb = nn.Embedding(num_users, embedding_dim)
        self.show_emb = nn.Embedding(num_shows, embedding_dim)

    def forward(self, user_ids, show_ids):
        u = self.user_emb(user_ids)
        s = self.show_emb(show_ids)
        return (u * s).sum(dim=1)  # dot product

# Training setup
model = Recommender(num_users, num_shows, embedding_dim)
optimizer = optim.Adam(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

# Convert data to tensors
user_ids = torch.tensor([u for u, s, r in interactions])
show_ids = torch.tensor([s for u, s, r in interactions])
ratings  = torch.tensor([r for u, s, r in interactions], dtype=torch.float)

# Training loop
for epoch in range(50):
    preds = model(user_ids, show_ids)
    loss = loss_fn(preds, ratings)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Training complete!")

# 🔮 Making recommendations
user_to_recommend = torch.tensor([0])  # user 0
all_shows = torch.arange(num_shows)

scores = model(user_to_recommend.repeat(num_shows), all_shows)
recommended = torch.topk(scores, k=2)  # top 2 shows
print("Recommended show IDs:", recommended.indices.tolist())
