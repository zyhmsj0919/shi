
from Basilisk.moduleTemplates import cModuleTemplate
from Basilisk.moduleTemplates import cppModuleTemplate
from Basilisk.utilities import SimulationBaseClass
from Basilisk.utilities import macros


def run():
    """
    Illustration of adding Basilisk modules to a task
    """

    #  Create a sim module as an empty container
    scSim = SimulationBaseClass.SimBaseClass()

    #  create the simulation process
    dynProcess = scSim.CreateNewProcess("dynamicsProcess")

    # create the dynamics task and specify the integration update time
    dynProcess.addTask(scSim.CreateNewTask("dynamicsTask", macros.sec2nano(5.)))#task有频率

    # create copies of the Basilisk modules
    mod1 = cModuleTemplate.cModuleTemplate()
    mod1.ModelTag = "cModule1"

    mod2 = cppModuleTemplate.CppModuleTemplate()
    mod2.ModelTag = "cppModule2"

    mod3 = cModuleTemplate.cModuleTemplate()
    mod3.ModelTag = "cModule3"

    scSim.AddModelToTask("dynamicsTask", mod1)
    scSim.AddModelToTask("dynamicsTask", mod2, 10)
    scSim.AddModelToTask("dynamicsTask", mod3, 5)

    #  initialize Simulation:
    scSim.InitializeSimulation()#初始化，dummy初始化为0，每执行一次task增加一次，只有task有频率
    print("InitializeSimulation() completed...")

    #   configure a simulation stop time and execute the simulation run
    scSim.ConfigureStopTime(macros.sec2nano(5.0))#设置停止时间
    scSim.ExecuteSimulation()#开始执行进程，执行两次任务
    #scSim.TotalSim.SingleStepProcesses()#执行一次task

    scSim.TotalSim.SingleStepProcesses()#执行第三次任务，单步执行任务
    print(mod1.dummy)#dummy=3

    1


    return


if __name__ == "__main__":
    run()