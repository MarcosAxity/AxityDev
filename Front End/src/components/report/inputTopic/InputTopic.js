import React, { useState } from "react";
import styles from "./InputTopic.module.css";
import { useForm } from "react-hook-form";
import ResultsDashboard from "../resultsDashboard/ResultsDashboard";

const InputTopic = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const [event, setEvent] = useState(false);

  const onSubmit = (data) => {
    console.log(data);
    if (data) {
      setEvent(true);
    }
  };

  return (
    <>
      <section className={styles.inputAndResult}>
        <section className={styles.input}>
          <div className={styles.textAboutTopic}>
            <h1 className={styles.text}>
              Danos un tema de tu interés que se esté tratando en Twitter y
              nosotros analizaremos si existen sesgos de género.
            </h1>
            <h1 className={styles.text}>
              Usa @ si quieres hacer una búsqueda por usuario, no uses #.
            </h1>
          </div>
          <form
            className={styles.fieldnbutton}
            onSubmit={handleSubmit(onSubmit)}
          >
            <div>
              <input
                type="text"
                className={styles.inputTopic}
                placeholder="Ingresa un tema"
                {...register("topic", {
                  required: {
                    value: true,
                    message: "Campo requerido",
                  },
                })}
              />
              {errors.topic && (
                <p className={styles.errorMessage}>{errors.topic.message}</p>
              )}
            </div>

            <button type="submit" className={styles.button}>
              Ver resultados
            </button>
          </form>
        </section>

        <div className={styles.resultsDashboard}>
          <ResultsDashboard event={event} />
        </div>
      </section>
    </>
  );
};
export default InputTopic;
