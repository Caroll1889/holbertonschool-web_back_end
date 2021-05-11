import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const upload = await uploadPhoto();
    const user = await createUser();
    return {
      upload,
      user,
    };
  } catch (err) {
    return {
      upload: null,
      user: null,
    };
  }
}
