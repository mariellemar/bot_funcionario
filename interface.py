import tkinter as tk
from tkinter import messagebox
from funcionarios import FuncionarioHora, FuncionarioFixo, FuncionarioComissao

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Funcionários")

        # Campo para Nome
        tk.Label(root, text="Nome:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1)

        # Campo para Matrícula
        tk.Label(root, text="Matrícula:").grid(row=1, column=0)
        self.matricula_entry = tk.Entry(root)
        self.matricula_entry.grid(row=1, column=1)

        # Tipo de Funcionário
        tk.Label(root, text="Tipo:").grid(row=2, column=0)
        self.tipo_var = tk.StringVar(value="hora")
        tk.Radiobutton(root, text="Horista", variable=self.tipo_var, value="hora").grid(row=2, column=1)
        tk.Radiobutton(root, text="Fixo", variable=self.tipo_var, value="fixo").grid(row=2, column=2)
        tk.Radiobutton(root, text="Comissionado", variable=self.tipo_var, value="comissao").grid(row=2, column=3)

        # Campos
        tk.Label(root, text="Horas Trabalhadas:").grid(row=3, column=0)
        self.horas_entry = tk.Entry(root)
        self.horas_entry.grid(row=3, column=1)

        tk.Label(root, text="Valor por Hora:").grid(row=4, column=0)
        self.valor_entry = tk.Entry(root)
        self.valor_entry.grid(row=4, column=1)

        tk.Label(root, text="Salário Mensal/Base:").grid(row=5, column=0)
        self.salario_entry = tk.Entry(root)
        self.salario_entry.grid(row=5, column=1)

        tk.Label(root, text="Vendas:").grid(row=6, column=0)
        self.vendas_entry = tk.Entry(root)
        self.vendas_entry.grid(row=6, column=1)

        tk.Label(root, text="Taxa de Comissão (%):").grid(row=7, column=0)
        self.taxa_entry = tk.Entry(root)
        self.taxa_entry.grid(row=7, column=1)

        self.update_fields()  # Inicializa os campos corretamente

        self.tipo_var.trace('w', self.update_fields)

        tk.Button(root, text="Calcular Salário", command=self.calcular_salario).grid(row=8, columnspan=2)

    def limpar_campos(self):
        """Limpa todos os campos de entrada."""
        self.horas_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.vendas_entry.delete(0, tk.END)
        self.taxa_entry.delete(0, tk.END)

    def update_fields(self, *args):
        tipo = self.tipo_var.get()

        self.limpar_campos()  # Limpa os campos ao trocar o tipo

        # Desativa todos os campos inicialmente
        self.horas_entry.config(state='disabled')
        self.valor_entry.config(state='disabled')
        self.salario_entry.config(state='disabled')
        self.vendas_entry.config(state='disabled')
        self.taxa_entry.config(state='disabled')

        # Habilita os campos conforme o tipo selecionado
        if tipo == "hora":
            self.horas_entry.config(state='normal')
            self.valor_entry.config(state='normal')
        if tipo == "fixo":
            self.salario_entry.config(state='normal')
        if tipo == "comissao":
            self.salario_entry.config(state='normal')
            self.vendas_entry.config(state='normal')
            self.taxa_entry.config(state='normal')

    def calcular_salario(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()

        tipo = self.tipo_var.get()

        try:
            if tipo == "hora":
                horas = float(self.horas_entry.get())
                valor = float(self.valor_entry.get())
                funcionario = FuncionarioHora(nome, matricula, horas, valor)
            elif tipo == "fixo":
                salario = float(self.salario_entry.get())
                funcionario = FuncionarioFixo(nome, matricula, salario)
            elif tipo == "comissao":
                salario = float(self.salario_entry.get())
                vendas = float(self.vendas_entry.get())
                taxa = float(self.taxa_entry.get())
                funcionario = FuncionarioComissao(nome, matricula, salario, vendas, taxa)

            salario_calculado = funcionario.calcular_salario()
            messagebox.showinfo("Salário Calculado", f"Salário de {nome}: R$ {salario_calculado:.2f}")

            self.nome_entry.delete(0, tk.END)
            self.matricula_entry.delete(0, tk.END)
            self.limpar_campos()

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)

    root.mainloop()
