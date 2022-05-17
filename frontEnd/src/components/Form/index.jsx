import React from 'react'
import { TextField, Box, Button } from "@mui/material"
import { useForm} from 'react-hook-form'


function Form() {
  const { register, handleSubmit, errors } = useForm()
  const onSubmit = data => console.log(data)

  return (
    <Box component='form' onSubmit={handleSubmit(onSubmit)}>
        <Box mb={2}>
          <TextField
            label='Nombre'
            helperText='Nombre de la compañia'
            color='primary'
            focused
            {...register("name", { required: true })}
          />
        </Box>
        <Box mb={2}>
          <TextField
            label='Dirección'
            helperText='Dirección de la compañia'
            color='primary'
            {...register("address", { required: true })}
          />
        </Box>
        <Box mb={2}>
          <TextField
            label='NIT'
            helperText='NIT de la compañia'
            color='primary'
            {...register("NIT", { required: true })}
          />
        </Box>
        <Box mb={2}>
          <TextField
            label='Teléfono'
            helperText='Teléfono de la compañia'
            color='primary'
            {...register("phone", { required: true })}
          />
        </Box>
        <Button onClick={handleSubmit(onSubmit)} variant="contained" color="success">Enviar</Button>
      </Box>
  )
}

export default Form