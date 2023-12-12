# 1.Zip the contents of this directory as pytorch_model.bin
```sh
zip -r model/pytorch_model.bin .
```
# 2. Install torch-model-archiver .
```sh
pip install torch-model-archiver
```
# 3.Create .mar file by running below command on terminal.
```sh
torch-model-archiver --model-name sentence_Transformer_BERT --version 1.0 --serialized-file pytorch_model.bin --handler run_handler.py --extra-files handler.py --export-path <output-path> --runtime python3 -f
```

# 4. Create a dockerfile packaging all the contents require to serve the model and start the server.

# 5. Build docker image
```sh
docker build -t ptserve-sbert:v1 dockerfile .
```

# 6. Run the container locally
```sh
docker run --rm -it -p 3000:8080 ptserve-sbert:v1
```


# References
https://yashna-shravani.medium.com/deploying-sbert-in-production-using-torchserve-cc1e438a90d