class MinhaPrimeiraThread extends Thread {
    private int quantidade;

    public MinhaPrimeiraThread(int quantidade) {
        this.quantidade = quantidade;
    }

    @Override
    public void run() {
        for (int i = 0; i < this.quantidade; i++) {
            System.out.println("Executando a thread: " + i);
        }
    }
}

class MinhaSegundaThread extends Thread {
    private int quantidade;

    public MinhaSegundaThread(int quantidade) {
        this.quantidade = quantidade;
    }

    @Override
    public void run() {
        for (int i = 0; i < this.quantidade; i++) {
            System.out.println("Executando a segunda thread: " + i);
        }
    }
}

public class Threads {
    public static void main(String[] args) {
        MinhaPrimeiraThread thread1 = new MinhaPrimeiraThread(100);
        MinhaSegundaThread thread2 = new MinhaSegundaThread(500);

        thread1.start();
        thread2.start();
    }
}