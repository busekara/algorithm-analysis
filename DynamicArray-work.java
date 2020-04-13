public class DynamicArray{
    
    int array[];
    int n; 
    int capacity;
    
    //yapıcı fonksiyon oluşturuldu.
    
    public DynamicArray(){
        array = new int[5]; //yapıcı fonksiyonda 5 elemanlı bir dizi oluşturduk.
        n = 0; //eklenecek eleman sayısı
        capacity = 5;
    }
    //sona eleman eklemek için append() fonksiyonu oluşturuldu.
    //en kötü senaryoda karmaşıklık = O(n)'dir.
    //bu nedenle en kötü senaryoda n eleman eklemek istersek karmaşıklık = n*O(n) olur.
    //n sayısı da etki etmediğinden karmaşıklık = O(n) olur.
    public void append(int value){
        //öncelikle bir kontrol ile başlıyoruz, eğer kapasiteden fazla sayı eklemek istenirse yeni dizi oluşturularak dizi genişletilir.
        if(n == capacity){
            
            int new_array[] = new int[capacity * 2]; //ideal olarak boyut iki katına çıkarıldı.
            //önceki dizideki elemanlar yeni diziye aktarılır.
            for(int i = 0; i < capacity; i++){
                new_array[i] = array[i];
            }
            
            //önceki değerler güncellenir.
            array = new_array;
            capacity = capacity * 2;
            
        }
        //if koşuluna girmediysek kapasite yeterlidir,direkt atama yapılır ayrıca if koşuluna girdiyse de bu kodlar çalışacak ve yeni değer diziye eklenecektir.
        array[n] = value ;
        n++ ; //eleman sayısı arttırıldı.
        
    }
    
    //sondan eleman silmek için remove() fonksiyonu oluşturuldu.
    //O(n)
    public void remove(){
        //eleman sayısı sıfırdan büyük ise silme işlemi uygulandı.
         if (n > 0) {
            array[n - 1] = 0;
            n--; //eleman sayısı azaltıldı.
        }
        
    }
    
    //boyut güncellenmesi için resize() fonksiyonu yazıldı.
    //O(n)
    public void resize(int new_size){
        
         int resize_array[] = new int[new_size]; //ideal olarak boyut iki katına çıkarıldı.
            //önceki dizideki elemanlar yeni diziye aktarılır.
            for(int i = 0; i < capacity; i++){
                resize_array[i] = array[i];
            }
            
            //önceki değerler güncellenir.
            array = resize_array;
            capacity = new_size;
        
    }

    public static void main(String []args){
         
        DynamicArray array = new DynamicArray();
         
        System.out.println("Array eleman sayısı:" + array.n + ", Array kapasite: " + array.capacity);
         
         //append() fonksiyonu çağırıldı.
        array.append(5);
        array.append(10);
        array.append(27);
        array.append(52);
        array.append(48);
        System.out.println("Array eleman sayısı:" + array.n + ", Array kapasite: " + array.capacity);
        //remove() fonksiyonu çağırıldı.
        array.remove();
        array.remove();
        array.remove();
        array.remove();
        array.remove();
        System.out.println("Array eleman sayısı:" + array.n + ", Array kapasite: " + array.capacity);
        //resize() fonksiyonu çağırıldı.
        array.resize(15);
        array.resize(30);
        array.resize(45);
        array.resize(60);
        array.resize(90);
        System.out.println("Array eleman sayısı:" + array.n + ", Array kapasite: " + array.capacity);
    }
}