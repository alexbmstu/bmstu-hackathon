****
## 2. Принцип действия электроэнцефалографа<a name="2"></a>


ЭЭГ представляет собой сложный колебательный электрический процесс, который может быть зарегистрирован при расположении электродов на мозге или на поверхности скальпа, и является результатом электрической суммации и фильтрации элементарных процессов, протекающих в нейронах головного мозга.



****
### 2.1. Основы электроэнцефалографии головного мозна человека <a name="21"></a>


Многочисленные исследования показывают, что электрические потенциалы отдельных нейронов головного мозга связаны тесной и достаточно точной количественной зависимостью с информационными процессами. Для того чтобы нейрон генерировал потенциал действия, передающий сообщение другим нейронам или эффекторным органам, необходимо, чтобы собственное его возбуждение достигло определенной пороговой величины.

Уровень возбуждения нейрона определяется суммой возбуждающих и тормозных воздействий, оказываемых на него в данный момент через синапсы. Если сумма возбуждающих воздействий больше суммы тормозных на величину, превышающую пороговый уровень, нейрон генерирует нервный импульс, распространяющийся затем по аксону. Описанным тормозным и возбуждающим процессам в нейроне и его отростках соответствуют определенной формы электрические потенциалы.

Как показано выше, электрическая активность отдельных нервных клеток отражает их функциональную активность по переработке и передаче информации. Отсюда можно сделать заключение, что суммарная ЭЭГ также в преформированном виде отражает функциональную активность, но уже не отдельных нервных клеток, а их громадных популяций, т.е., иначе говоря, функциональную активность мозга. Это положение, получившее многочисленные неоспоримые доказательства, представляется исключительно важным для анализа ЭЭГ, поскольку дает ключ к пониманию того, какие системы мозга определяют внешний вид и внутреннюю организацию ЭЭГ.

![Основные отделы головного мозга человека](assets/brain.png)
**Основные отделы головного мозга человека**


****
### 2.2. Восьмиканальный электроэнцефалограф ИНЭУМ им.И.С.Брука <a name="22"></a>


Электроэнцефалограф производства компании ИНЭУМ им.И.С.Брука представляют собой многоканальные регистрирующие устройства, объединяющие 8 идентичных усилительно-регистрирующих блоков (каналов), позволяющих таким образом регистрировать одномоментно электрическую активность от соответствующего числа пар электродов, установленных на голове обследуемого.

Электроэнцефалограф ООО ИНЭУМ им.И.С.Брука цифрового типа с сухими эоектродами преобразуют ЭЭГ в цифровую форму и вводят ее в микроконтроллер STM32, который управляет  непрерывный процесс регистрации ЭЭГ, одновременно записываемой в память компьютера.

![Электроэнцефалограф ИНЭУМ им.И.С.Брука](assets/eeg.jpg)
**Электроэнцефалограф ИНЭУМ им.И.С.Брука**	


Микроконтроллер STM32 реализует систему генерации управления исполнительными механизмами и потоковую передачу данных по протоколу MODICON MODBUS RTU. 
Протокол реализован на физических линиях интерейса RS232 через микросхему FTDI, транслирущую пакеты RS232 в `USB`. Таким образом, прием и передача пакетов ЭЭГ может босуществяться по интерфейсу USB. 

Для получения доступа к отснятым или уже обработанным данным необходимо выдать ряд команд инициализации, а также команд запросов в формате, представленном ниже:


![Формат пакета запроса](assets/burst.jpg)
**Формат пакета запроса**

В ответ на команды, электроэнцефалограф генерирует следующую последовательность данных. 

![Формат пакета ответа](assets/burst1.jpg)
**Формат пакета ответа**


Ниже приведен код инициализации электроэнцефалографа. 

```
ser = serial.Serial("/dev/ttyUSB0")
ser.baudrate = 460800

if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()

ser.write("/put/memory?address=39&value=214&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=40&value=194&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=41&value=96&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=42&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=43&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=44&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=45&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=46&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=47&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=48&value=112&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=49&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=50&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=51&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=87&value=0x76543210&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=88&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=89&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=90&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=91&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=92&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=93&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=94&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=95&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=39&value=214&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=40&value=194&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=41&value=96&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=42&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=43&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=44&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=45&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=46&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=47&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=48&value=112&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=49&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=50&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=51&value=0&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=87&value=0x76543210&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=88&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=89&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=90&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=91&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=92&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=93&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=94&value=0x40&\r".encode())
time.sleep(5)
ser.write("/put/memory?address=95&value=0x40&\r".encode())
time.sleep(5)

ser.write("/put/memory?address=52&value=1&\r".encode())
print ("wait 3s and all be ok!")
time.sleep(3)


```

