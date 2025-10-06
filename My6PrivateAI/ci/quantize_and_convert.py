import torch

def convert_model(pytorch_path, gguf_path):
    print(f"Converting {pytorch_path} -> {gguf_path}")
    torch.save({"weights": "dummy"}, gguf_path)

if __name__ == "__main__":
    convert_model("models/model_weights_placeholder/base.pt", "models/model_weights_placeholder/model.gguf")