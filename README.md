# Projeto de Detecção de Rostos

Este é um projeto simples de detecção de rostos usando OpenCV em Python. O objetivo é carregar uma imagem, detectar rostos nela e destacá-los com retângulos.

## Descrição

O projeto consiste em um script Python que utiliza a biblioteca OpenCV para a detecção de rostos em uma imagem. Ao executar o script, o programa carrega uma imagem específica do diretório `inputs`, converte-a para escala de cinza e, em seguida, utiliza um classificador pré-treinado para identificar rostos na imagem. Os rostos detectados são destacados com retângulos vermelhos, e a imagem resultante é exibida.

## Como Executar

1. Certifique-se de ter Python 3.x instalado.
2. Instale a biblioteca OpenCV com o seguinte comando:

    ```bash
    pip install opencv-python
    ```

3. Clone o repositório:

    ```bash
    git clone https://seurepositorio.com/seuprojeto.git
    ```

4. Navegue até o diretório do projeto:

    ```bash
    cd seuprojeto
    ```

5. Execute o script:

    ```bash
    python script.py
    ```

O script processará a imagem e exibirá a janela com os rostos detectados.

## Personalização

- **Imagens de Entrada:** Adicione suas próprias imagens ao diretório `inputs`.
- **Parâmetros de Detecção:** Experimente ajustar os parâmetros de detecção em `detect_faces` no script `script.py` para obter melhores resultados.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests.

## Licença

Este projeto é licenciado sob a [Sua Licença Aqui]. Consulte o arquivo LICENSE para obter mais detalhes.
