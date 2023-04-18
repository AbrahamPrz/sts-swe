CHECKPOINT = 'symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli'


def main(args=None):
    from transformers import AutoConfig

    # Se selecciona un modelo de la libreria de Hugging Face para tareas de STS en español
    model_config = AutoConfig.from_pretrained(CHECKPOINT)
    print(type(model_config))
    # El resultado es una configuración XLMRoberta


    from transformers import XLMRobertaModel, XLMRobertaConfig

    config_base = XLMRobertaConfig()
    config_pretrained = XLMRobertaConfig.from_pretrained(CHECKPOINT)
    model_base = XLMRobertaModel(config_base)
    model_pretrained = XLMRobertaModel(config_pretrained)
    print(f'Base model config: \n{config_base}')
    print(f'Pretrained model config: \n{config_pretrained}')


    from transformers import XLMRobertaModel

    model = XLMRobertaModel.from_pretrained(CHECKPOINT)
    model.save_pretrained('my_model')


if __name__ == '__main__':
    main()