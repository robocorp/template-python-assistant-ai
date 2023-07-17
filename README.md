# Template: Python - Assistant AI Chat

This template leverages the new Python open-source structure [robo](https://github.com/robocorp/robo), the [libraries](https://github.com/robocorp/robo#libraries) from to same project as well.
The full power of [rpaframework](https://github.com/robocorp/rpaframework) is also available for you on Python as a backup while we implement new Python libraries.

The template provides you with the basic structure of an Assistant project: a chat interface that allows the user to communicate with a GPT model. The environment contains the most used libraries, so you do not have to start thinking about those right away.

To get the Assistant running, you will need an Open AI API key in the Control Room Vault.
Firstly, follow the [Open AI documentation](https://platform.openai.com/docs/quickstart/build-your-application) to generate an API key and copy it's value.
Then go to Control Room and create a new Vault Secret as desribed in [Our Guide](https://robocorp.com/docs/development-guide/variables-and-secrets/vault).
The Secret name will be `openai` and the key will be `key`.

👉 After running the bot, check out the `log.html` under the `output` -folder.

The template shows you how to use Robocorp Vault for your secrets and how to create robots that interact with humans and AI models, in this case OpenAI's GPT.

Do note that with Robocorp tooling you:
- Do NOT need Python installed
- Should NOT be writing `pip install..`; the [conda.yaml](https://github.com/robocorp/template-python/blob/master/conda.yaml) is here for a reason.
- You do not need to worry about Python's main -functions and, most importantly, the logging setup

🚀 Now, go get'em

For more information, do not forget to check out the following:
* [Robocorp Documentation -site](https://robocorp.com/docs)
* [Portal for more examples](https://robocorp.com/portal)
* [robo repo](https://github.com/robocorp/robo) as this will developed a lot...
