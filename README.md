# croissantage
Une appliquette simple sous docker permettant de croissanter des collègues de bureau !

# Build du container : 
- se placer dans le dépot.

``` sudo docker build -t croissantage . ```

# Lancement du docker : 

``` sudo docker run --rm -p 8080:8080 -v $MON_REPO_CLONÉ/app:/app croissantage ```
